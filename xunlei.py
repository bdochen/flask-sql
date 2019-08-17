package com.xunlei.common.member.p036b;

import android.content.SharedPreferences.Editor;
import android.os.Bundle;
import android.text.TextUtils;
import com.alipay.sdk.packet.C0227d;
import com.xunlei.common.base.XLLog;
import com.xunlei.common.encrypt.CharsetConvert;
import com.xunlei.common.encrypt.HextoChar;
import com.xunlei.common.encrypt.MD5;
import com.xunlei.common.encrypt.RsaEncode;
import com.xunlei.common.member.XLErrorCode;
import com.xunlei.common.member.XLOnUserListener;
import com.xunlei.common.member.XLUserInfo.USERINFOKEY;
import com.xunlei.common.member.p035a.C1453b;
import com.xunlei.common.member.p035a.C1456d;
import com.xunlei.common.member.p035a.C1456d.C1457a;
import com.xunlei.common.member.p035a.C1465k;
import java.io.UnsupportedEncodingException;
import java.net.SocketException;
import java.net.SocketTimeoutException;
import java.net.UnknownHostException;
import org.apache.http.client.HttpResponseException;
import org.json.JSONException;
import org.json.JSONObject;

/* renamed from: com.xunlei.common.member.b.g */
/* compiled from: UserLoginTask */
public final class C1506g extends C1526o {

    /* renamed from: a */
    private static String f4758a = "pubKey";

    /* renamed from: b */
    private String f4759b = "";

    /* renamed from: c */
    private String f4760c = "";

    /* renamed from: d */
    private String f4761d = "";

    /* renamed from: e */
    private String f4762e = "";

    /* renamed from: f */
    private String f4763f = "";

    /* renamed from: g */
    private int f4764g = 0;

    public C1506g(C1465k kVar) {
        super(kVar);
    }

    /* renamed from: a */
    public final void mo8585a() {
        super.mo8585a();
        this.f4759b = "";
        this.f4760c = "";
        this.f4762e = "";
        this.f4763f = "";
    }

    /* renamed from: a */
    public final void mo8597a(String str, boolean z) {
        this.f4759b = str;
        this.f4764g = z ? 1 : 0;
        XLLog.m8433v("UserLoginTask", "put user name = " + str + "#is auto login(1->auto) = " + this.f4764g);
    }

    /* renamed from: a */
    public final void mo8596a(String str, String str2) {
        this.f4761d = str2;
        XLLog.m8433v("UserLoginTask", "putPassword encrypt = " + str);
        if (this.f4764g == 0) {
            this.f4760c = MD5.encrypt(str);
        } else {
            this.f4760c = str;
        }
        mo8625h().mo8462a(USERINFOKEY.EncryptedPassword, this.f4760c);
    }

    /* renamed from: b */
    public final void mo8598b(String str, String str2) {
        this.f4762e = str;
        this.f4763f = str2;
        if (str != null) {
            XLLog.m8433v("UserLoginTask", "user verify code info: key = " + str + " #code = " + str2);
        }
    }

    /* renamed from: d */
    private String m8747d() {
        return mo8624g().mo8506h().getSharedPreferences("pubKey", 0).getString("Moudle", "AC69F5CCC8BDE47CD3D371603748378C9CFAD2938A6B021E0E191013975AD683F5CBF9ADE8BD7D46B4D2EC2D78AF146F1DD2D50DC51446BB8880B8CE88D476694DFC60594393BEEFAA16F5DBCEBE22F89D640F5336E42F587DC4AFEDEFEAC36CF007009CCCE5C1ACB4FF06FBA69802A8085C2C54BADD0597FC83E6870F1E36FD");
    }

    /* renamed from: n */
    private String m8748n() {
        return mo8624g().mo8506h().getSharedPreferences("pubKey", 0).getString("Exponent", "010001");
    }

    /* renamed from: c */
    public final void mo8600c(String str, String str2) {
        Editor edit = mo8624g().mo8506h().getSharedPreferences("pubKey", 0).edit();
        edit.putString("Exponent", str2);
        edit.putString("Moudle", str);
        edit.commit();
    }

    /* renamed from: c */
    public final String mo8599c() {
        return this.f4760c;
    }

    /* renamed from: o */
    private boolean m8749o() {
        if (this.f4761d.compareTo(mo8624g().mo8510l()) == 0) {
            return true;
        }
        return false;
    }

    /* renamed from: a */
    public final boolean mo8589a(XLOnUserListener xLOnUserListener, Bundle bundle) {
        if (xLOnUserListener == null || bundle == null || bundle.getString(C0227d.f405o) != "userLoginTask") {
            return false;
        }
        XLLog.m8433v("UserLoginTask", "before call onUserLogin");
        int i = bundle.getInt("errorCode");
        if (m8831e(i)) {
            C1456d.m8552a(mo8624g().mo8506h(), C1457a.f4617c);
        }
        if (m8832f(i)) {
            mo8625h().clearUserData();
        }
        return xLOnUserListener.onUserLogin(i, mo8625h(), mo8626i(), bundle.getString("errorDesc"), mo8627j());
    }

    /* renamed from: b */
    public final boolean mo8590b() {
        boolean z;
        boolean z2 = false;
        if (C1527a.f4834d == mo8623f()) {
            return z2;
        }
        if (TextUtils.isEmpty(this.f4759b)) {
            Bundle bundle = new Bundle();
            bundle.putString(C0227d.f405o, "userLoginTask");
            bundle.putInt("errorCode", 2);
            bundle.putString("errorDesc", "账号不存在");
            mo8624g().mo8483a((C1526o) this, bundle);
            mo8621d(C1527a.f4833c);
            return z2;
        } else if (this.f4760c.compareTo(MD5.encrypt("")) == 0) {
            Bundle bundle2 = new Bundle();
            bundle2.putString(C0227d.f405o, "userLoginTask");
            bundle2.putInt("errorCode", 3);
            bundle2.putString("errorDesc", "密码错误");
            mo8624g().mo8483a((C1526o) this, bundle2);
            mo8621d(C1527a.f4833c);
            return z2;
        } else {
            if (this.f4761d != null && !TextUtils.isEmpty(this.f4761d)) {
                if (this.f4761d.compareTo(mo8624g().mo8510l()) == 0) {
                    z = true;
                } else {
                    z = z2;
                }
                if (!z) {
                    Bundle bundle3 = new Bundle();
                    bundle3.putString(C0227d.f405o, "userLoginTask");
                    bundle3.putInt("errorCode", 16777216);
                    bundle3.putString("errorDesc", "用户识别码错误");
                    mo8624g().mo8483a((C1526o) this, bundle3);
                    mo8621d(C1527a.f4833c);
                    return z2;
                }
            }
            mo8621d(C1527a.f4832b);
            JSONObject jSONObject = new JSONObject();
            try {
                jSONObject.put("protocolVersion", 108);
                jSONObject.put("sequenceNo", mo8627j());
                jSONObject.put("platformVersion", 1);
                jSONObject.put("peerID", mo8628k());
                jSONObject.put("businessType", mo8624g().mo8500d());
                jSONObject.put("clientVersion", mo8624g().mo8503e());
                jSONObject.put("isCompressed", 0);
                jSONObject.put("cmdID", 1);
                jSONObject.put("userName", this.f4759b);
                byte[] encodeUseRSA = RsaEncode.encodeUseRSA(this.f4760c.getBytes(), m8747d(), m8748n());
                jSONObject.put("passWord", new String(HextoChar.bytes_to_hex(encodeUseRSA, encodeUseRSA.length)));
                jSONObject.put("loginType", this.f4764g);
                jSONObject.put("sessionID", "");
                jSONObject.put("verifyKey", this.f4762e);
                jSONObject.put("verifyCode", this.f4763f);
                jSONObject.put("appName", "ANDROID-" + mo8624g().mo8511m());
                jSONObject.put("devicesign", C1540u.m8896b());
                jSONObject.put("sdkVersion", mo8624g().mo8504f());
                JSONObject jSONObject2 = new JSONObject();
                jSONObject2.put("e", m8748n());
                jSONObject2.put("n", m8747d());
                jSONObject.put("rsaKey", jSONObject2);
                jSONObject.put("extensionList", "");
                StringBuffer stringBuffer = new StringBuffer();
                stringBuffer.append("user login start:account = ").append(this.f4759b).append("#befor RSA psw = ").append(this.f4760c).append("#psw check sum").append(this.f4761d).append("#login type = ").append(this.f4764g);
                XLLog.m8433v("UserLoginTask", stringBuffer.toString());
                String jSONObject3 = jSONObject.toString();
                XLLog.m8433v("UserLoginTask", jSONObject3);
                try {
                    mo8624g().mo8508j().mo8439a(jSONObject3.getBytes(CharsetConvert.GBK), 1, (C1453b) new C1453b() {
                        /* renamed from: a */
                        public final void mo8444a(String str) {
                            XLLog.m8433v("UserLoginTask", str);
                            try {
                                JSONObject jSONObject = new JSONObject(str);
                                XLLog.m8433v("UserLoginTask", "result json objet = " + jSONObject.toString());
                                int i = jSONObject.getInt("errorCode");
                                if (i == 0) {
                                    C1465k.m8583a().mo8518v();
                                    C1506g.this.mo8625h().clearUserData();
                                    XLLog.m8433v("UserLoginTask", "start to obtain xl user info.");
                                    jSONObject.put("passwordCheckNum", C1506g.this.mo8624g().mo8510l());
                                    jSONObject.put("encryptedPassword", C1506g.this.mo8599c());
                                    C1506g.this.mo8625h().mo8464a(jSONObject);
                                    C1506g.this.mo8625h().dump();
                                    String optString = jSONObject.optString("loginKey");
                                    XLLog.m8433v("UserLoginTask", "save auto login info.");
                                    C1456d dVar = new C1456d(C1506g.this.mo8625h().getIntValue(USERINFOKEY.UserID), C1506g.this.mo8625h().getStringValue(USERINFOKEY.EncryptedPassword), C1506g.this.mo8625h().getStringValue(USERINFOKEY.PasswordCheckNum), optString);
                                    int i2 = C1457a.f4617c;
                                    if (TextUtils.isEmpty(optString)) {
                                        i2 = C1457a.f4615a;
                                    }
                                    C1456d.m8553a(dVar, C1506g.this.mo8624g().mo8506h(), i2);
                                    C1506g.this.mo8625h().mo8461a(C1506g.this.mo8624g().mo8506h());
                                    Bundle bundle = new Bundle();
                                    bundle.putString(C0227d.f405o, "userLoginTask");
                                    bundle.putInt("errorCode", 0);
                                    bundle.putString("errorDesc", "");
                                    C1506g.this.mo8624g().mo8483a((C1526o) C1506g.this, bundle);
                                    if (C1506g.this.mo8623f() != C1527a.f4834d) {
                                        C1506g.this.mo8624g().mo8484a(true, 0);
                                    }
                                } else if (i == 7) {
                                    Bundle bundle2 = new Bundle();
                                    bundle2.putString(C0227d.f405o, "userLoginTask");
                                    bundle2.putInt("errorCode", i);
                                    bundle2.putString("errorDesc", jSONObject.optString("errorDesc"));
                                    C1506g.this.mo8624g().mo8483a((C1526o) C1506g.this, bundle2);
                                    return;
                                } else if (i == 6) {
                                    String optString2 = jSONObject.optString("verifyType");
                                    if (!TextUtils.isEmpty(optString2)) {
                                        C1506g.this.mo8624g().mo8499c(optString2);
                                    }
                                    XLLog.m8433v("UserLoginTask", "get verify code type = " + optString2);
                                    Bundle bundle3 = new Bundle();
                                    bundle3.putString(C0227d.f405o, "userLoginTask");
                                    bundle3.putInt("errorCode", 6);
                                    bundle3.putString("errorDesc", jSONObject.optString("errorDesc"));
                                    C1506g.this.mo8624g().mo8483a((C1526o) C1506g.this, bundle3);
                                    return;
                                } else {
                                    if (i == 9) {
                                        JSONObject jSONObject2 = jSONObject.getJSONObject("rsaKey");
                                        String optString3 = jSONObject2.optString("e");
                                        String optString4 = jSONObject2.optString("n");
                                        String optString5 = jSONObject2.optString("md5");
                                        StringBuilder sb = new StringBuilder();
                                        sb.append(optString3);
                                        sb.append(optString4);
                                        if (optString5.compareTo(MD5.encrypt(sb.toString())) == 0) {
                                            Editor edit = C1506g.this.mo8624g().mo8506h().getSharedPreferences("pubKey", 0).edit();
                                            edit.putString("Exponent", optString3);
                                            edit.putString("Moudle", optString4);
                                            edit.commit();
                                            C1506g.this.mo8590b();
                                            return;
                                        }
                                    }
                                    Bundle bundle4 = new Bundle();
                                    bundle4.putString(C0227d.f405o, "userLoginTask");
                                    bundle4.putInt("errorCode", i);
                                    bundle4.putString("errorDesc", jSONObject.optString("errorDesc"));
                                    C1506g.this.mo8624g().mo8483a((C1526o) C1506g.this, bundle4);
                                }
                            } catch (JSONException e) {
                                e.printStackTrace();
                                Bundle bundle5 = new Bundle();
                                bundle5.putString(C0227d.f405o, "userLoginTask");
                                bundle5.putInt("errorCode", XLErrorCode.UNPACKAGE_ERROR);
                                bundle5.putString("errorDesc", "服务器返回数据解包过程出现异常");
                                C1506g.this.mo8624g().mo8483a((C1526o) C1506g.this, bundle5);
                            }
                            C1506g.this.mo8621d(C1527a.f4833c);
                        }

                        /* renamed from: a */
                        public final void mo8445a(Throwable th) {
                            XLLog.m8430e("UserLoginTask", "error = " + th.getMessage());
                            int i = XLErrorCode.UNKNOWN_ERROR;
                            if (th instanceof UnknownHostException) {
                                i = XLErrorCode.UNKNOWN_HOST_ERROR;
                            }
                            if (th instanceof SocketException) {
                                i = XLErrorCode.SOCKET_ERROR;
                            }
                            if (th instanceof SocketTimeoutException) {
                                i = XLErrorCode.SOCKET_TIMEOUT_ERROR;
                            }
                            if (th instanceof HttpResponseException) {
                                i = ((HttpResponseException) th).getStatusCode();
                            }
                            Bundle bundle = new Bundle();
                            bundle.putString(C0227d.f405o, "userLoginTask");
                            bundle.putInt("errorCode", i);
                            bundle.putString("errorDesc", "当前网络不可用，请稍后登陆");
                            C1506g.this.mo8624g().mo8483a((C1526o) C1506g.this, bundle);
                            C1506g.this.mo8621d(C1527a.f4833c);
                        }
                    }, mo8627j());
                    return true;
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                    Bundle bundle4 = new Bundle();
                    bundle4.putString(C0227d.f405o, "userLoginTask");
                    bundle4.putInt("errorCode", 16777215);
                    bundle4.putString("errorDesc", "组包过程中出现异常");
                    mo8624g().mo8483a((C1526o) this, bundle4);
                    mo8621d(C1527a.f4833c);
                    return z2;
                }
            } catch (JSONException e2) {
                e2.printStackTrace();
                Bundle bundle5 = new Bundle();
                bundle5.putString(C0227d.f405o, "userLoginTask");
                bundle5.putInt("errorCode", 16777215);
                bundle5.putString("errorDesc", "组包过程中出现异常");
                mo8624g().mo8483a((C1526o) this, bundle5);
                mo8621d(C1527a.f4833c);
                return z2;
            }
        }
    }
}
