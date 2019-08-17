package com.xunlei.common.member.p035a;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.os.Bundle;
import com.xunlei.common.base.XLLog;
import com.xunlei.common.base.XLUtilTools;
import com.xunlei.common.httpclient.BaseHttpClientListener;
import com.xunlei.common.member.p036b.C1540u;
import java.io.UnsupportedEncodingException;
import java.security.KeyManagementException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.UnrecoverableKeyException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import org.apache.http.Header;
import org.apache.http.conn.ssl.SSLSocketFactory;
import org.apache.http.cookie.ClientCookie;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

/* renamed from: com.xunlei.common.member.a.a */
/* compiled from: AsyncHttpProxy */
public final class C1448a {

    /* renamed from: a */
    private static final String f4575a = "portalCache";

    /* renamed from: g */
    private static final C1448a f4576g = new C1448a();

    /* renamed from: b */
    private long f4577b = 432000000;

    /* renamed from: c */
    private final String f4578c;

    /* renamed from: d */
    private final String f4579d;

    /* renamed from: e */
    private final String f4580e;

    /* renamed from: f */
    private final int f4581f;
    /* access modifiers changed from: private */
    @SuppressLint({"UseSparseArrays"})

    /* renamed from: h */
    public Map<Integer, List<String>> f4582h = new HashMap();
    /* access modifiers changed from: private */

    /* renamed from: i */
    public int f4583i = 0;

    /* renamed from: j */
    private int f4584j = 0;

    /* renamed from: k */
    private boolean f4585k = false;

    /* renamed from: l */
    private int f4586l = 1000000;

    /* renamed from: m */
    private List<C1453b> f4587m = new ArrayList();
    /* access modifiers changed from: private */

    /* renamed from: n */
    public Context f4588n = null;

    /* renamed from: o */
    private String f4589o = "1.0.0";

    /* renamed from: p */
    private int f4590p = 0;
    /* access modifiers changed from: private */

    /* renamed from: q */
    public String f4591q = "AsyncHttpProxy";

    /* renamed from: r */
    private int f4592r = 0;

    /* renamed from: com.xunlei.common.member.a.a$a */
    /* compiled from: AsyncHttpProxy */
    public class C1450a {

        /* renamed from: i */
        private static int f4594i = 108;

        /* renamed from: j */
        private static String f4595j = "AC69F5CCC8BDE47CD3D371603748378C9CFAD2938A6B021E0E191013975AD683F5CBF9ADE8BD7D46B4D2EC2D78AF146F1DD2D50DC51446BB8880B8CE88D476694DFC60594393BEEFAA16F5DBCEBE22F89D640F5336E42F587DC4AFEDEFEAC36CF007009CCCE5C1ACB4FF06FBA69802A8085C2C54BADD0597FC83E6870F1E36FD";

        /* renamed from: k */
        private static String f4596k = "010001";

        /* renamed from: a */
        byte[] f4597a;

        /* renamed from: b */
        int f4598b;

        /* renamed from: c */
        int f4599c;

        /* renamed from: d */
        int f4600d;

        /* renamed from: e */
        int f4601e;

        /* renamed from: f */
        C1453b f4602f;

        /* renamed from: g */
        int f4603g;

        public C1450a() {
            this.f4597a = null;
            this.f4598b = 1;
            this.f4599c = 0;
            this.f4600d = 0;
            this.f4601e = 0;
            this.f4602f = null;
            this.f4603g = C1448a.this.mo8442c();
        }

        /* renamed from: a */
        public final void mo8449a(byte[] bArr) {
            this.f4597a = bArr;
        }

        /* renamed from: a */
        public final void mo8447a(int i) {
            this.f4598b = i;
        }

        /* renamed from: b */
        public final void mo8450b(int i) {
            this.f4601e = i;
        }

        /* renamed from: a */
        public final void mo8448a(C1453b bVar) {
            this.f4602f = bVar;
        }

        /* renamed from: b */
        private static boolean m8541b() {
            if (C1465k.m8583a().mo8517u() != 0) {
                return false;
            }
            C1465k.m8583a().mo8502d(1);
            return true;
        }

        /* renamed from: a */
        private void m8539a(String str) {
            if (this.f4601e != 0) {
                C1459f fVar = new C1459f();
                fVar.f4622a = XLUtilTools.getServerDomain(str);
                fVar.f4623b = this.f4599c + (this.f4600d * 3);
                C1465k.m8583a().mo8479a(this.f4601e, fVar);
            }
        }

        /* access modifiers changed from: private */
        /* renamed from: b */
        public String m8540b(byte[] bArr) {
            String str = "";
            try {
                return new String(bArr, "ISO-8859-1");
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
                XLLog.m8433v(C1448a.this.f4591q, "transformSingleCharString error = " + e.getMessage());
                return str;
            }
        }

        /* renamed from: a */
        public final void mo8446a() {
            final String a;
            boolean z = true;
            if (this.f4598b == 7) {
                if (C1465k.m8583a().mo8517u() == 0) {
                    C1465k.m8583a().mo8502d(1);
                } else {
                    z = false;
                }
                if (!z) {
                    XLLog.m8433v("AsyncHttpProxyReq", "go home boy!");
                    return;
                } else {
                    XLLog.m8433v("AsyncHttpProxyReq", "go ahead boy!");
                    a = C1448a.this.mo8435a(this.f4598b, C1448a.this.f4583i);
                }
            } else {
                a = C1448a.this.mo8435a(this.f4598b, this.f4603g);
            }
            if (a == null) {
                a = "https://login.mobile.reg2t.sandai.net:443";
            }
            XLLog.m8433v(C1448a.this.f4591q, "send request use url = " + a + "#request=" + hashCode());
            if (a.contains("login.mobile.reg2t.sandai.net")) {
                new Thread(new Runnable() {
                    public final void run() {
                        XLLog.m8433v(C1448a.this.f4591q, "login.mobile.reg2t.sandai.net -> ip address = " + XLUtilTools.getHostAddress("login.mobile.reg2t.sandai.net"));
                    }
                }).start();
            }
            C1465k.m8583a().mo8509k().post(C1448a.this.f4588n, a, null, this.f4597a, new BaseHttpClientListener() {
                public final void onSuccess(int i, Header[] headerArr, byte[] bArr) {
                    String a = C1450a.this.m8540b(bArr);
                    if (C1450a.this.f4598b == 1) {
                        try {
                            JSONObject jSONObject = new JSONObject(a);
                            if (jSONObject.getInt("errorCode") != 8 || C1450a.this.f4599c >= 3) {
                                C1450a.this.f4599c = 0;
                                if (jSONObject.has("errorIsRetry") && jSONObject.getInt("errorIsRetry") != 0 && C1450a.this.f4600d < C1448a.this.mo8434a(C1450a.this.f4598b)) {
                                    C1450a.this.f4603g = (C1450a.this.f4603g + 1) % C1448a.this.mo8434a(C1450a.this.f4598b);
                                    C1450a.this.f4600d++;
                                    Bundle bundle = new Bundle();
                                    bundle.putString("type", "onRetry");
                                    bundle.putInt("count", C1450a.this.f4600d);
                                    bundle.putString("address", C1448a.this.mo8435a(C1450a.this.f4598b, C1450a.this.f4603g));
                                    C1448a.this.mo8437a(bundle);
                                    C1450a.this.mo8446a();
                                } else if (C1450a.this.f4602f != null) {
                                    C1450a.m8538a(C1450a.this, a);
                                    C1450a.this.f4602f.mo8444a(a);
                                }
                            } else {
                                C1450a.this.f4599c++;
                                Bundle bundle2 = new Bundle();
                                bundle2.putString("type", "onRetry");
                                bundle2.putInt("count", C1450a.this.f4599c);
                                C1448a.this.mo8437a(bundle2);
                                C1450a.this.mo8446a();
                            }
                        } catch (JSONException e) {
                            if (C1450a.this.f4602f != null) {
                                C1450a.m8538a(C1450a.this, a);
                                C1450a.this.f4602f.mo8445a((Throwable) e);
                            }
                            e.printStackTrace();
                        }
                    } else if (C1450a.this.f4598b == 7) {
                        try {
                            if (new JSONObject(a).getInt("errorCode") != 0) {
                                if (C1450a.this.f4600d < C1448a.this.mo8434a(C1450a.this.f4598b)) {
                                    C1448a.this.f4583i = (C1448a.this.f4583i + 1) % C1448a.this.mo8434a(C1450a.this.f4598b);
                                    C1450a.this.f4600d++;
                                    C1450a.this.mo8446a();
                                }
                            } else if (C1450a.this.f4602f != null) {
                                C1450a.m8538a(C1450a.this, a);
                                C1450a.this.f4602f.mo8444a(a);
                            }
                        } catch (JSONException e2) {
                            e2.printStackTrace();
                        }
                    } else if (C1450a.this.f4602f != null) {
                        C1450a.m8538a(C1450a.this, a);
                        C1450a.this.f4602f.mo8444a(a);
                    }
                }

                public final void onFailure(Throwable th, byte[] bArr) {
                    if (C1450a.this.f4598b == 7) {
                        if (C1450a.this.f4600d < C1448a.this.mo8434a(C1450a.this.f4598b)) {
                            C1450a.this.f4603g = (C1450a.this.f4603g + 1) % C1448a.this.mo8434a(C1450a.this.f4598b);
                            C1450a.this.f4600d++;
                            C1450a.this.mo8446a();
                            XLLog.m8429d(C1448a.this.f4591q, th.getMessage() + "portal重试    次数：" + C1450a.this.f4600d + "#request=" + hashCode());
                        }
                    } else if (C1450a.this.f4600d < C1448a.this.mo8434a(C1450a.this.f4598b)) {
                        C1450a.this.f4603g = (C1450a.this.f4603g + 1) % C1448a.this.mo8434a(C1450a.this.f4598b);
                        C1450a.this.f4600d++;
                        Bundle bundle = new Bundle();
                        bundle.putString("type", "onRetry");
                        bundle.putInt("count", C1450a.this.f4600d);
                        bundle.putString("address", C1448a.this.mo8435a(C1450a.this.f4598b, C1450a.this.f4603g));
                        C1448a.this.mo8437a(bundle);
                        C1450a.this.mo8446a();
                        XLLog.m8429d(C1448a.this.f4591q, th.getMessage() + "请求重试    次数：" + C1450a.this.f4600d);
                    } else if (C1450a.this.f4602f != null) {
                        C1450a.m8538a(C1450a.this, a);
                        C1450a.this.f4602f.mo8445a(th);
                    }
                }
            });
        }

        /* renamed from: a */
        static /* synthetic */ void m8538a(C1450a aVar, String str) {
            if (aVar.f4601e != 0) {
                C1459f fVar = new C1459f();
                fVar.f4622a = XLUtilTools.getServerDomain(str);
                fVar.f4623b = aVar.f4599c + (aVar.f4600d * 3);
                C1465k.m8583a().mo8479a(aVar.f4601e, fVar);
            }
        }
    }

    private C1448a() {
    }

    /* renamed from: e */
    private static SSLSocketFactory m8521e() {
        KeyStore keyStore;
        KeyStoreException e;
        C1454c cVar;
        NoSuchAlgorithmException e2;
        UnrecoverableKeyException e3;
        KeyManagementException e4;
        try {
            keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
            try {
                keyStore.load(null, null);
            } catch (Exception e5) {
                e = e5;
                e.printStackTrace();
                cVar = new C1454c(keyStore);
                cVar.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);
                return cVar;
            }
        } catch (Exception e6) {
            e = e6;
            keyStore = null;
            e.printStackTrace();
            cVar = new C1454c(keyStore);
            cVar.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);
            return cVar;
        }
        try {
            cVar = new C1454c(keyStore);
            try {
                cVar.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);
            } catch (KeyManagementException e7) {
                e4 = e7;
                e4.printStackTrace();
                return cVar;
            } catch (UnrecoverableKeyException e8) {
                e3 = e8;
                e3.printStackTrace();
                return cVar;
            } catch (NoSuchAlgorithmException e9) {
                e2 = e9;
                e2.printStackTrace();
                return cVar;
            } catch (KeyStoreException e10) {
                e = e10;
                e.printStackTrace();
                return cVar;
            }
        } catch (KeyManagementException e11) {
            e4 = e11;
            cVar = null;
            e4.printStackTrace();
            return cVar;
        } catch (UnrecoverableKeyException e12) {
            e3 = e12;
            cVar = null;
            e3.printStackTrace();
            return cVar;
        } catch (NoSuchAlgorithmException e13) {
            e2 = e13;
            cVar = null;
            e2.printStackTrace();
            return cVar;
        } catch (KeyStoreException e14) {
            e = e14;
            cVar = null;
            e.printStackTrace();
            return cVar;
        }
        return cVar;
    }

    /* JADX WARNING: Removed duplicated region for block: B:17:0x00ab  */
    /* JADX WARNING: Removed duplicated region for block: B:45:? A[RETURN, SYNTHETIC] */
    /* renamed from: a */
    /* Code decompiled incorrectly, please refer to instructions dump. */
    public final void mo8436a(android.content.Context r8, int r9, java.lang.String r10) {
        /*
            r7 = this;
            r1 = 1
            r2 = 0
            r5 = 0
            boolean r0 = r7.f4585k
            if (r0 == 0) goto L_0x0008
        L_0x0007:
            return
        L_0x0008:
            r7.f4585k = r1
            r7.f4588n = r8
            r7.f4589o = r10
            r7.f4590p = r9
            r7.f4583i = r5
            r7.f4584j = r5
            android.content.Context r0 = r7.f4588n
            java.lang.String r1 = "portalCache"
            android.content.SharedPreferences r0 = r0.getSharedPreferences(r1, r5)
            java.lang.String r1 = "PortalSrvList"
            java.lang.String r3 = "[{\"port\":\"443\",\"type\":\"https\",\"ip\":\"119.147.41.25\"}]"
            java.lang.String r1 = r0.getString(r1, r3)
            java.lang.String r3 = "LoginSrvList"
            java.lang.String r4 = "[{\"port\":\"443\",\"type\":\"https\",\"ip\":\"123.150.173.56\"},{\"port\":\"443\",\"type\":\"https\",\"ip\":\"119.147.41.25\"},{\"port\":\"443\",\"type\":\"https\",\"ip\":\"125.39.70.56\"}]"
            java.lang.String r0 = r0.getString(r3, r4)
            org.json.JSONArray r3 = new org.json.JSONArray     // Catch:{ JSONException -> 0x00b2 }
            r3.<init>(r1)     // Catch:{ JSONException -> 0x00b2 }
            java.util.List r1 = m8509a(r3)     // Catch:{ JSONException -> 0x00b2 }
            r3 = 0
            java.lang.String r4 = "https://login.mobile.reg2t.sandai.net:443"
            r1.add(r3, r4)     // Catch:{ JSONException -> 0x00b2 }
            java.util.Map<java.lang.Integer, java.util.List<java.lang.String>> r3 = r7.f4582h     // Catch:{ JSONException -> 0x00b2 }
            r4 = 7
            java.lang.Integer r4 = java.lang.Integer.valueOf(r4)     // Catch:{ JSONException -> 0x00b2 }
            r3.put(r4, r1)     // Catch:{ JSONException -> 0x00b2 }
            org.json.JSONArray r1 = new org.json.JSONArray     // Catch:{ JSONException -> 0x00b2 }
            r1.<init>(r0)     // Catch:{ JSONException -> 0x00b2 }
            java.util.List r0 = m8509a(r1)     // Catch:{ JSONException -> 0x00b2 }
            r1 = 0
            java.lang.String r3 = "https://login.mobile.reg2t.sandai.net:443"
            r0.add(r1, r3)     // Catch:{ JSONException -> 0x00b2 }
            java.util.Map<java.lang.Integer, java.util.List<java.lang.String>> r1 = r7.f4582h     // Catch:{ JSONException -> 0x00b2 }
            r3 = 1
            java.lang.Integer r3 = java.lang.Integer.valueOf(r3)     // Catch:{ JSONException -> 0x00b2 }
            r1.put(r3, r0)     // Catch:{ JSONException -> 0x00b2 }
        L_0x005e:
            java.util.ArrayList r0 = new java.util.ArrayList
            r0.<init>()
            java.lang.String r1 = "http://dy.cdn.vip.xunlei.com:80/fcg-bin/cgi_query_capacity.fcg?userid="
            r0.add(r5, r1)
            java.util.Map<java.lang.Integer, java.util.List<java.lang.String>> r1 = r7.f4582h
            r3 = 9
            java.lang.Integer r3 = java.lang.Integer.valueOf(r3)
            r1.put(r3, r0)
            java.util.ArrayList r0 = new java.util.ArrayList
            r0.<init>()
            java.lang.String r1 = "http://dynamic.cloud.vip.xunlei.com/interface/query_user_info?uid="
            r0.add(r5, r1)
            java.util.Map<java.lang.Integer, java.util.List<java.lang.String>> r1 = r7.f4582h
            r3 = 10
            java.lang.Integer r3 = java.lang.Integer.valueOf(r3)
            r1.put(r3, r0)
            java.lang.String r0 = java.security.KeyStore.getDefaultType()     // Catch:{ Exception -> 0x00b7 }
            java.security.KeyStore r0 = java.security.KeyStore.getInstance(r0)     // Catch:{ Exception -> 0x00b7 }
            r1 = 0
            r3 = 0
            r0.load(r1, r3)     // Catch:{ Exception -> 0x00f2 }
        L_0x0095:
            com.xunlei.common.member.a.c r1 = new com.xunlei.common.member.a.c     // Catch:{ KeyManagementException -> 0x00be, UnrecoverableKeyException -> 0x00c6, NoSuchAlgorithmException -> 0x00ce, KeyStoreException -> 0x00d6 }
            r1.<init>(r0)     // Catch:{ KeyManagementException -> 0x00be, UnrecoverableKeyException -> 0x00c6, NoSuchAlgorithmException -> 0x00ce, KeyStoreException -> 0x00d6 }
            org.apache.http.conn.ssl.X509HostnameVerifier r0 = org.apache.http.conn.ssl.SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER     // Catch:{ KeyManagementException -> 0x00ed, UnrecoverableKeyException -> 0x00e8, NoSuchAlgorithmException -> 0x00e3, KeyStoreException -> 0x00de }
            r1.setHostnameVerifier(r0)     // Catch:{ KeyManagementException -> 0x00ed, UnrecoverableKeyException -> 0x00e8, NoSuchAlgorithmException -> 0x00e3, KeyStoreException -> 0x00de }
        L_0x009f:
            com.xunlei.common.member.a.k r0 = com.xunlei.common.member.p035a.C1465k.m8583a()
            com.xunlei.common.httpclient.BaseHttpClient r0 = r0.mo8509k()
            boolean r2 = r0 instanceof com.xunlei.common.httpclient.AsyncHttpClient
            if (r2 == 0) goto L_0x0007
            com.xunlei.common.httpclient.AsyncHttpClient r0 = (com.xunlei.common.httpclient.AsyncHttpClient) r0
            r0.setSSLSocketFactory(r1)
            goto L_0x0007
        L_0x00b2:
            r0 = move-exception
            r0.printStackTrace()
            goto L_0x005e
        L_0x00b7:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x00ba:
            r1.printStackTrace()
            goto L_0x0095
        L_0x00be:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x00c1:
            r1.printStackTrace()
            r1 = r0
            goto L_0x009f
        L_0x00c6:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x00c9:
            r1.printStackTrace()
            r1 = r0
            goto L_0x009f
        L_0x00ce:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x00d1:
            r1.printStackTrace()
            r1 = r0
            goto L_0x009f
        L_0x00d6:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x00d9:
            r1.printStackTrace()
            r1 = r0
            goto L_0x009f
        L_0x00de:
            r0 = move-exception
            r6 = r0
            r0 = r1
            r1 = r6
            goto L_0x00d9
        L_0x00e3:
            r0 = move-exception
            r6 = r0
            r0 = r1
            r1 = r6
            goto L_0x00d1
        L_0x00e8:
            r0 = move-exception
            r6 = r0
            r0 = r1
            r1 = r6
            goto L_0x00c9
        L_0x00ed:
            r0 = move-exception
            r6 = r0
            r0 = r1
            r1 = r6
            goto L_0x00c1
        L_0x00f2:
            r1 = move-exception
            goto L_0x00ba
        */
        throw new UnsupportedOperationException("Method not decompiled: com.xunlei.common.member.p035a.C1448a.mo8436a(android.content.Context, int, java.lang.String):void");
    }

    /* JADX WARNING: Removed duplicated region for block: B:12:0x0024  */
    /* JADX WARNING: Removed duplicated region for block: B:38:? A[RETURN, SYNTHETIC] */
    /* renamed from: f */
    /* Code decompiled incorrectly, please refer to instructions dump. */
    private static void m8522f() {
        /*
            r2 = 0
            java.lang.String r0 = java.security.KeyStore.getDefaultType()     // Catch:{ Exception -> 0x002a }
            java.security.KeyStore r0 = java.security.KeyStore.getInstance(r0)     // Catch:{ Exception -> 0x002a }
            r1 = 0
            r3 = 0
            r0.load(r1, r3)     // Catch:{ Exception -> 0x0065 }
        L_0x000e:
            com.xunlei.common.member.a.c r1 = new com.xunlei.common.member.a.c     // Catch:{ KeyManagementException -> 0x0031, UnrecoverableKeyException -> 0x0039, NoSuchAlgorithmException -> 0x0041, KeyStoreException -> 0x0049 }
            r1.<init>(r0)     // Catch:{ KeyManagementException -> 0x0031, UnrecoverableKeyException -> 0x0039, NoSuchAlgorithmException -> 0x0041, KeyStoreException -> 0x0049 }
            org.apache.http.conn.ssl.X509HostnameVerifier r0 = org.apache.http.conn.ssl.SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER     // Catch:{ KeyManagementException -> 0x0060, UnrecoverableKeyException -> 0x005b, NoSuchAlgorithmException -> 0x0056, KeyStoreException -> 0x0051 }
            r1.setHostnameVerifier(r0)     // Catch:{ KeyManagementException -> 0x0060, UnrecoverableKeyException -> 0x005b, NoSuchAlgorithmException -> 0x0056, KeyStoreException -> 0x0051 }
        L_0x0018:
            com.xunlei.common.member.a.k r0 = com.xunlei.common.member.p035a.C1465k.m8583a()
            com.xunlei.common.httpclient.BaseHttpClient r0 = r0.mo8509k()
            boolean r2 = r0 instanceof com.xunlei.common.httpclient.AsyncHttpClient
            if (r2 == 0) goto L_0x0029
            com.xunlei.common.httpclient.AsyncHttpClient r0 = (com.xunlei.common.httpclient.AsyncHttpClient) r0
            r0.setSSLSocketFactory(r1)
        L_0x0029:
            return
        L_0x002a:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x002d:
            r1.printStackTrace()
            goto L_0x000e
        L_0x0031:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x0034:
            r1.printStackTrace()
            r1 = r0
            goto L_0x0018
        L_0x0039:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x003c:
            r1.printStackTrace()
            r1 = r0
            goto L_0x0018
        L_0x0041:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x0044:
            r1.printStackTrace()
            r1 = r0
            goto L_0x0018
        L_0x0049:
            r0 = move-exception
            r1 = r0
            r0 = r2
        L_0x004c:
            r1.printStackTrace()
            r1 = r0
            goto L_0x0018
        L_0x0051:
            r0 = move-exception
            r4 = r0
            r0 = r1
            r1 = r4
            goto L_0x004c
        L_0x0056:
            r0 = move-exception
            r4 = r0
            r0 = r1
            r1 = r4
            goto L_0x0044
        L_0x005b:
            r0 = move-exception
            r4 = r0
            r0 = r1
            r1 = r4
            goto L_0x003c
        L_0x0060:
            r0 = move-exception
            r4 = r0
            r0 = r1
            r1 = r4
            goto L_0x0034
        L_0x0065:
            r1 = move-exception
            goto L_0x002d
        */
        throw new UnsupportedOperationException("Method not decompiled: com.xunlei.common.member.p035a.C1448a.m8522f():void");
    }

    /* renamed from: a */
    public static void m8510a() {
    }

    /* renamed from: b */
    public static C1448a m8516b() {
        return f4576g;
    }

    /* access modifiers changed from: private */
    /* renamed from: a */
    public static List<String> m8509a(JSONArray jSONArray) {
        ArrayList arrayList = new ArrayList();
        if (jSONArray == null) {
            return arrayList;
        }
        int i = 0;
        while (true) {
            int i2 = i;
            if (i2 >= jSONArray.length()) {
                return arrayList;
            }
            JSONObject jSONObject = (JSONObject) jSONArray.opt(i2);
            if (jSONObject != null) {
                arrayList.add(jSONObject.optString("type") + "://" + jSONObject.optString("ip") + ":" + jSONObject.optString(ClientCookie.PORT_ATTR));
            }
            i = i2 + 1;
        }
    }

    /* renamed from: g */
    private void m8523g() {
        SharedPreferences sharedPreferences = this.f4588n.getSharedPreferences(f4575a, 0);
        String string = sharedPreferences.getString("PortalSrvList", "[{\"port\":\"443\",\"type\":\"https\",\"ip\":\"119.147.41.25\"}]");
        String string2 = sharedPreferences.getString("LoginSrvList", "[{\"port\":\"443\",\"type\":\"https\",\"ip\":\"123.150.173.56\"},{\"port\":\"443\",\"type\":\"https\",\"ip\":\"119.147.41.25\"},{\"port\":\"443\",\"type\":\"https\",\"ip\":\"125.39.70.56\"}]");
        try {
            List a = m8509a(new JSONArray(string));
            a.add(0, "https://login.mobile.reg2t.sandai.net:443");
            this.f4582h.put(Integer.valueOf(7), a);
            List a2 = m8509a(new JSONArray(string2));
            a2.add(0, "https://login.mobile.reg2t.sandai.net:443");
            this.f4582h.put(Integer.valueOf(1), a2);
        } catch (JSONException e) {
            e.printStackTrace();
        }
        ArrayList arrayList = new ArrayList();
        arrayList.add(0, "http://dy.cdn.vip.xunlei.com:80/fcg-bin/cgi_query_capacity.fcg?userid=");
        this.f4582h.put(Integer.valueOf(9), arrayList);
        ArrayList arrayList2 = new ArrayList();
        arrayList2.add(0, "http://dynamic.cloud.vip.xunlei.com/interface/query_user_info?uid=");
        this.f4582h.put(Integer.valueOf(10), arrayList2);
    }

    /* renamed from: a */
    private boolean m8514a(C1453b bVar) {
        if (this.f4587m.contains(bVar)) {
            return false;
        }
        this.f4587m.add(bVar);
        return true;
    }

    /* renamed from: a */
    public final void mo8437a(Bundle bundle) {
        Iterator it = this.f4587m.iterator();
        while (it.hasNext()) {
            it.next();
            if (bundle.getString("type").equalsIgnoreCase("onRetry")) {
                bundle.getInt("count");
                bundle.getString("address");
            }
        }
    }

    /* renamed from: b */
    private boolean m8517b(C1453b bVar) {
        return this.f4587m.remove(bVar);
    }

    /* renamed from: c */
    public final synchronized int mo8442c() {
        return this.f4584j;
    }

    /* renamed from: c */
    private synchronized void m8519c(int i) {
        this.f4584j = i;
    }

    /* renamed from: a */
    public final synchronized int mo8434a(int i) {
        if (i != 7) {
            i = 1;
        }
        return ((List) this.f4582h.get(Integer.valueOf(i))).size();
    }

    /* renamed from: a */
    public final String mo8435a(int i, int i2) {
        if (i != 7) {
            i = 1;
        }
        List list = (List) this.f4582h.get(Integer.valueOf(i));
        if (list == null || i2 < 0 || i2 >= list.size()) {
            return "https://login.mobile.reg2t.sandai.net:443";
        }
        return (String) list.get(i2);
    }

    /* renamed from: a */
    private void m8511a(String str, byte[] bArr, BaseHttpClientListener baseHttpClientListener) {
        C1465k.m8583a().mo8509k().post(this.f4588n, str, null, bArr, baseHttpClientListener);
    }

    /* renamed from: a */
    public final void mo8440a(Header[] headerArr, String str, byte[] bArr, BaseHttpClientListener baseHttpClientListener) {
        C1465k.m8583a().mo8509k().post(this.f4588n, str, headerArr, bArr, baseHttpClientListener);
    }

    /* renamed from: a */
    private void m8513a(byte[] bArr, int i, C1453b bVar) {
        C1450a aVar = new C1450a();
        aVar.f4597a = bArr;
        aVar.f4602f = bVar;
        aVar.f4598b = 7;
        aVar.mo8446a();
    }

    /* renamed from: a */
    public final void mo8439a(byte[] bArr, int i, C1453b bVar, int i2) {
        C1450a aVar = new C1450a();
        aVar.f4597a = bArr;
        aVar.f4602f = bVar;
        aVar.f4598b = i;
        aVar.f4601e = i2;
        aVar.mo8446a();
    }

    /* renamed from: a */
    public final void mo8438a(String str, BaseHttpClientListener baseHttpClientListener) {
        C1465k.m8583a().mo8509k().get(this.f4588n, str, null, baseHttpClientListener);
    }

    /* renamed from: a */
    private void m8512a(String str, Header[] headerArr, BaseHttpClientListener baseHttpClientListener) {
        C1465k.m8583a().mo8509k().get(this.f4588n, str, headerArr, baseHttpClientListener);
    }

    /* renamed from: d */
    public final void mo8443d() {
        if ((System.currentTimeMillis() - this.f4588n.getSharedPreferences(f4575a, 0).getLong("PrePortalTime", 0)) - this.f4577b >= 0) {
            m8524h();
        }
    }

    /* renamed from: h */
    private boolean m8524h() {
        try {
            JSONObject jSONObject = new JSONObject();
            jSONObject.put("protocolVersion", 108);
            int i = this.f4586l + 1;
            this.f4586l = i;
            jSONObject.put("sequenceNo", i);
            jSONObject.put("platformVersion", 1);
            jSONObject.put("businessType", this.f4590p);
            jSONObject.put("clientVersion", this.f4589o);
            jSONObject.put("isCompressed", 0);
            jSONObject.put("cmdID", 17);
            jSONObject.put("userID", "");
            jSONObject.put("sessionID", "");
            int i2 = this.f4592r + 1;
            this.f4592r = i2;
            jSONObject.put("portalCount", i2);
            jSONObject.put("appName", "ANDROID-" + C1465k.m8583a().mo8511m());
            jSONObject.put("devicesign", C1540u.m8896b());
            jSONObject.put("sdkVersion", C1465k.m8583a().mo8504f());
            byte[] bytes = jSONObject.toString().getBytes();
            C14491 r1 = new C1453b() {
                /* renamed from: a */
                public final void mo8444a(String str) {
                    try {
                        JSONObject jSONObject = new JSONObject(str.toString());
                        if (jSONObject.getInt("errorCode") == 0) {
                            Editor edit = C1448a.this.f4588n.getSharedPreferences(C1448a.f4575a, 0).edit();
                            JSONArray optJSONArray = jSONObject.optJSONArray("loginSrvIpList");
                            List a = C1448a.m8509a(optJSONArray);
                            if (a.size() > 0) {
                                a.add(0, "https://login.mobile.reg2t.sandai.net:443");
                                C1448a.this.f4582h.put(Integer.valueOf(1), a);
                                edit.putString("LoginSrvList", optJSONArray.toString());
                            }
                            JSONArray optJSONArray2 = jSONObject.optJSONArray("portalSrvIpList");
                            List a2 = C1448a.m8509a(optJSONArray2);
                            if (a2.size() > 0) {
                                a2.add(0, "https://login.mobile.reg2t.sandai.net:443");
                                C1448a.this.f4582h.put(Integer.valueOf(7), a2);
                                edit.putString("PortalSrvList", optJSONArray2.toString());
                            }
                            edit.putLong("PrePortalTime", System.currentTimeMillis());
                            edit.commit();
                        }
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }

                /* renamed from: a */
                public final void mo8445a(Throwable th) {
                    super.mo8445a(th);
                }
            };
            C1450a aVar = new C1450a();
            aVar.f4597a = bytes;
            aVar.f4602f = r1;
            aVar.f4598b = 7;
            aVar.mo8446a();
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return true;
    }

    /* renamed from: b */
    public final String mo8441b(int i) {
        String str = "";
        List list = (List) this.f4582h.get(Integer.valueOf(i));
        if (list != null) {
            return (String) list.get(0);
        }
        return str;
    }
}
