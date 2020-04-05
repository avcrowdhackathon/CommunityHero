package com.panwise.smsgateway;


import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.telephony.SmsMessage;
import android.util.Log;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.JsonRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class SmsBroadcastReceiver extends BroadcastReceiver {
    private final String BASE_URL = "https://rhubarb-cake-22341.herokuapp.com/api/v1/";
    private static final String SMS_RECEIVED = "android.provider.Telephony.SMS_RECEIVED";
    static HashMap<String, Boolean> registering = new HashMap<>();

    @Override
    public void onReceive(Context context, Intent intent) {

        Log.d("ON ", "RECEIVE");
        Bundle bundle = intent.getExtras();
        Object[] messages = (Object[]) bundle.get("pdus");
        SmsMessage[] sms = new SmsMessage[messages.length];
        // Create messages for each incoming PDU
        for (int n = 0; n < messages.length; n++) {
            sms[n] = SmsMessage.createFromPdu((byte[]) messages[n]);
        }
        for (final SmsMessage msg : sms) {
            String contents = msg.getMessageBody().toLowerCase();
            if (contents.contains("register") || contents.contains("sign up") || contents.contains("join") || contents.contains("account") || contents.contains("sign me up")) {
                registering.put(msg.getOriginatingAddress(), true);
                sendSms(msg.getOriginatingAddress(), "Please reply to this message by sending your location.");
            }
            else if(registering.get(msg.getOriginatingAddress())!=null && registering.get(msg.getOriginatingAddress())){
                registering.put(msg.getOriginatingAddress(), false);
                Log.e("in", "here");

                final String url = BASE_URL + "sms/register/";
                final RequestQueue queue = Volley.newRequestQueue(context);

                // Lookup location to nominatim
                Log.e("url", "https://nominatim.openstreetmap.org/search/" + URLEncoder.encode("kalavryton 9 aglantzia") + "?format=json");
                StringRequest locationRequest = new StringRequest(Request.Method.GET, "https://nominatim.openstreetmap.org/search/" + URLEncoder.encode(msg.getMessageBody()).replace("+", "%20") + "?format=json",
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {
                                try {
                                    Log.e("in", "nominatim response");
                                    Log.e("response", response);
                                    JSONArray j = new JSONArray(response);
                                    final String lat = j.getJSONObject(0).getString("lat");
                                    final String lng = j.getJSONObject(0).getString("lon");
                                    StringRequest stringRequest = new StringRequest(Request.Method.POST, url,
                                            new Response.Listener<String>() {
                                                @Override
                                                public void onResponse(String response) {
                                                    Log.e("response", response);
                                                    sendSms(msg.getOriginatingAddress(), "You are now registered! You can send in orders using SMS at any time.");

                                                }
                                            }, new Response.ErrorListener() {
                                        @Override
                                        public void onErrorResponse(VolleyError error) {
                                            Log.e("ERROR", error.toString());
                                        }
                                    }) {
                                        @Override
                                        public byte[] getBody() {
                                            return ("{\"from\": \"" + msg.getOriginatingAddress() + "\", \"lat\": \""+ lat + "\", \"lng\": \"" + lng +"\"}").getBytes();
                                        }
                                    };
                                    queue.add(stringRequest);
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                                Log.e("response", response);
                                // your response

                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e("ERROR", error.toString());
                    }
                });
                queue.add(locationRequest);


            }
            else {
                final String url = BASE_URL + "sms/order/";
                final RequestQueue queue = Volley.newRequestQueue(context);
                Map<String, String> m = new HashMap<>();
                m.put("from", msg.getOriginatingAddress());
                m.put("content", msg.getMessageBody());
                JsonObjectRequest orderRequest = new JsonObjectRequest(url, new JSONObject(m),
                        new Response.Listener<JSONObject>() {
                            @Override
                            public void onResponse(JSONObject response) {
                                try {
                                    if(!response.get("status").toString().equals("ok")) {
                                        sendSms(msg.getOriginatingAddress(), "You are not registered. Please reply with your home address to register");
                                        registering.put(msg.getOriginatingAddress(), true);
                                    }
                                    else{
                                        try {
                                            String message = "";
                                            String[] m = msg.getMessageBody().split("\n");
                                            for(int i=0;i<m.length;i++){
                                                message+=m[i] + ": " + response.getJSONArray("items").getString(i) + '\n';
                                            }
                                            message+="Total cost: " + response.getString("cost");
                                            message+="\nYou can confirm or change your order here: ";
                                            message+="http://46.251.98.58:8000/cart.html?user=\n"+response.getString("userID");
                                            sendSms(msg.getOriginatingAddress(), message);
                                        } catch (JSONException e) {
                                            e.printStackTrace();
                                        }
                                    }
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                                Log.e("response", response.toString());
                            }
                        }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Log.e("ERROR", error.toString());
                    }
                });
                orderRequest.setRetryPolicy(new DefaultRetryPolicy(
                        0,
                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));

                queue.add(orderRequest);

            }
            Log.e("RECEIVED MSG", ":" + msg.getMessageBody());
            // Verify if the message came from our known sender

        }
    }

    private void sendSms(String addr, String mess){
        SmsManager sms = SmsManager.getDefault();
        ArrayList<String> parts = sms.divideMessage(mess);
        sms.sendMultipartTextMessage(addr, null, parts, null,
                null);}
}