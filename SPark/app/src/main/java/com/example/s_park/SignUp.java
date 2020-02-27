package com.example.s_park;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

import com.google.firebase.analytics.FirebaseAnalytics;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class SignUp extends AppCompatActivity {
    FirebaseAnalytics mFirebaseAnalytics;
    EditText Email_1 , Phone_no , pwsd_1 ,con_pwsd_1 ;
    Button SignUp_1 ;
    String E_mail;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);
        mFirebaseAnalytics = FirebaseAnalytics.getInstance(this);
        Email_1 = (EditText) findViewById(R.id.email);
        Phone_no = (EditText) findViewById(R.id.phone);
        pwsd_1 = (EditText) findViewById(R.id.createPassword);
        con_pwsd_1 = (EditText) findViewById(R.id.confirmPassword);
        SignUp_1 = (Button) findViewById(R.id.Signup);

        E_mail = Email_1.getText().toString();
        FirebaseDatabase database = FirebaseDatabase.getInstance();
        DatabaseReference myRef = database.getReference(E_mail);
        myRef.child("Phone").setValue(Phone_no.toString());

    }
}
