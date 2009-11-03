# $Id$
# Authority: dag

Summary: The Mono CIL runtime, suitable for running .NET code
Name: mono
Version: 1.0.6
Release: 1%{?dist}
License: LGPL
Group: Development/Tools
URL: http://www.go-mono.com/

Source: http://www.go-mono.com/archive/%{version}/mono-%{version}.tar.gz
Patch: mono-remove-gacdir-flag.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, glib2-devel >= 1.3.11, pkgconfig, libicu-devel
BuildRequires: gcc-c++
#BuildRequires: rsync, j2sdk

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package core
Summary: The Mono CIL runtime, suitable for running .NET code
Group: Development/Tools

Provides: mono
Obsoletes: mono <= %{version}-%{release}
Obsoletes: mono-drawing <= %{version}-%{release}, mono-cairo <= %{version}-%{release}
Obsoletes: mono-xml-relaxng <= %{version}-%{release}, mono-posix <= %{version}-%{release}
Obsoletes: mono-ziplib <= %{version}-%{release}, mono-nunit <= %{version}-%{release}

%description core
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine (as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

%package basic
Summary: Mono's VB runtime
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description basic
Mono's VB runtime

%package ikvm
Summary: Support for IKVM
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description ikvm
Support for IKVM

%package winforms
Summary: Mono's Windows Forms implementation
Group: Development/Tools
Requires: mono-core = %{version}-%{release}
Provides: mono-window-forms
Obsoletes: mono-window-forms <= %{version}-%{release}

%description winforms
Mono's Windows Forms implementation

%package web
Summary: Mono implementation of ASP.NET, Remoting and Web Services
Group: Development/Tools
Requires: mono-core = %{version}-%{release}
Obsoletes: mono-web-forms <= %{version}-%{release}, mono-web-services <= %{version}-%{release}
Obsoletes: mono-remoting <= %{version}-%{release}

%description web
Mono implementation of ASP.NET, Remoting and Web Services

%package extras
Summary: Extra packages
Group: Development/Tools
Requires: mono-core = %{version}-%{release}
Obsoletes: mono-ms-extras <= %{version}-%{release}

%description extras
Extra packages

%package -n ibm-data-db2
Summary: Database connectivity for DB2
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description -n ibm-data-db2
Database connectivity for DB2

%package devel
Summary: Development tools for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}
Obsoletes: mono-peapi <= %{version}-%{release}, mono-runtime-devel <= %{version}-%{release}
Obsoletes: mono-core-devel <= %{version}-%{release}, mono-complete-devel %{version}-%{release}

%description devel
Development tools for Mono

%package data-oracle
Summary: Database connectivity for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description data-oracle
Database connectivity for Mono

%package data
Summary: Database connectivity for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}
Obsoletes: mono-ms-enterprise <= %{version}-%{release}, mono-novell-directory <= %{version}-%{release}
Obsoletes: mono-directory <= %{version}-%{release}

%description data
Database connectivity for Mono

%package locale-extras
Summary: Extra Locale information
Group: Development/Tools
Requires: mono-core = %{version}-%{release}
Obsoletes: mono-locale-cjk <= %{version}-%{release}, mono-locale-mideast <= %{version}-%{release}
Obsoletes: mono-locale-other <= %{version}-%{release}, mono-locale-rare <= %{version}-%{release}

%description locale-extras
Extra Locale information

%package data-postgresql
Summary: Database connectivity for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description data-postgresql
Database connectivity for Mono

%package -n bytefx-data-mysql
Summary: Database connectivity for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description -n bytefx-data-mysql
Database connectivity for Mono

%package data-sybase
Summary: Database connectivity for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description data-sybase
Database connectivity for Mono

%package data-sqlite
Summary: Database connectivity for Mono
Group: Development/Tools
Requires: mono-core = %{version}-%{release}

%description data-sqlite
Database connectivity for Mono

%package complete
Summary: This package contains all runtime Mono packages
Group: Development/Tools
Requires: bytefx-data-mysql = %{version}-%{release}
Requires: ibm-data-db2 = %{version}-%{release}
Requires: mono-basic = %{version}-%{release}
Requires: mono-core = %{version}-%{release}
Requires: mono-data = %{version}-%{release}
Requires: mono-data-oracle = %{version}-%{release}
Requires: mono-data-postgresql = %{version}-%{release}
Requires: mono-data-sqlite = %{version}-%{release}
Requires: mono-data-sybase = %{version}-%{release}
Requires: mono-extras = %{version}-%{release}
#Requires: mono-ikvm = %{version}-%{release}
Requires: mono-locale-extras = %{version}-%{release}
Requires: mono-web = %{version}-%{release}

%description complete
This package contains all runtime Mono packages

%prep
%setup
%patch -p1 -P 0

%build
%configure \
	--with-ikvm="yes" \
	--with-signaltstack="no" \
	--with-jdk="/usr/java/j2sdk1.4.2_04"
#	--with-nptl="no"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files core
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING.LIB NEWS README
%doc %{_mandir}/man1/certmgr.1*
%doc %{_mandir}/man1/chktrust.1*
%doc %{_mandir}/man1/gacutil.1*
%doc %{_mandir}/man1/mcs.1*
%doc %{_mandir}/man1/mint.1*
%doc %{_mandir}/man5/mono-config.5*
%doc %{_mandir}/man1/mono.1*
%doc %{_mandir}/man1/setreg.1*
%doc %{_mandir}/man1/sn.1*
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/1.0/
%dir %{_libdir}/mono/gac/
%{_sysconfdir}/mono/config
%{_sysconfdir}/mono/machine.config
%{_bindir}/certmgr*
%{_bindir}/chktrust*
%{_bindir}/gacutil*
%{_bindir}/mcs
%{_bindir}/mint
%{_bindir}/mono
%{_bindir}/mono-find-provides*
%{_bindir}/mono-find-requires*
%{_bindir}/setreg*
%{_bindir}/sn*
%{_libdir}/libmint.so*
%{_libdir}/libmono.so*
%{_libdir}/libMonoPosixHelper.so*
%{_libdir}/mono/*/mcs.exe
%{_libdir}/mono/*/cscompmgd*
%{_libdir}/mono/1.0/Commons.Xml.Relaxng.dll
%{_libdir}/mono/gac/Commons.Xml.Relaxng/
%{_libdir}/mono/1.0/I18N.dll
%{_libdir}/mono/gac/I18N/
%{_libdir}/mono/1.0/I18N.West.dll
%{_libdir}/mono/gac/I18N.West/
%{_libdir}/mono/1.0/ICSharpCode.SharpZipLib.dll
%{_libdir}/mono/gac/ICSharpCode.SharpZipLib/
%{_libdir}/mono/1.0/Microsoft.VisualC.dll
%{_libdir}/mono/gac/Microsoft.VisualC/
%{_libdir}/mono/1.0/Mono.Cairo.dll
%{_libdir}/mono/gac/Mono.Cairo/
%{_libdir}/mono/1.0/Mono.CSharp.Debugger.dll
%{_libdir}/mono/gac/Mono.CSharp.Debugger/
%{_libdir}/mono/1.0/Mono.GetOptions.dll
%{_libdir}/mono/gac/Mono.GetOptions/
%{_libdir}/mono/1.0/Mono.Posix.dll
%{_libdir}/mono/gac/Mono.Posix/
%{_libdir}/mono/1.0/Mono.Security.dll
%{_libdir}/mono/gac/Mono.Security/
%{_libdir}/mono/1.0/System.dll
%{_libdir}/mono/gac/System/
%{_libdir}/mono/1.0/System.Drawing.dll
%{_libdir}/mono/gac/System.Drawing/
%{_libdir}/mono/1.0/System.Security.dll
%{_libdir}/mono/gac/System.Security/
%{_libdir}/mono/1.0/System.Xml.dll
%{_libdir}/mono/gac/System.Xml/
%{_libdir}/mscorlib.dll
%{_libdir}/mono/1.0/Mono.Security.Win32.dll
%{_libdir}/mono/1.0/nunit.core.dll
%{_libdir}/mono/1.0/nunit.framework.dll
%{_libdir}/mono/1.0/nunit.util.dll
%exclude %{_datadir}/libgc-mono/

%files -n bytefx-data-mysql
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/ByteFX.Data.dll
%{_libdir}/mono/gac/ByteFX.Data/

%files -n ibm-data-db2
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/IBM.Data.DB2.dll
%{_libdir}/mono/gac/IBM.Data.DB2/

%files basic
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_bindir}/mbas
%{_libdir}/mono/1.0/mbas.exe
%{_libdir}/mono/1.0/Microsoft.VisualBasic.dll
%{_libdir}/mono/gac/Microsoft.VisualBasic/

%files data
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/sqlsharp.1*
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_bindir}/sqlsharp*
%{_libdir}/mono/1.0/Mono.Data.Tds.dll
%{_libdir}/mono/gac/Mono.Data.Tds/
%{_libdir}/mono/1.0/Mono.Data.TdsClient.dll
%{_libdir}/mono/gac/Mono.Data.TdsClient/
%{_libdir}/mono/1.0/System.Data.dll
%{_libdir}/mono/gac/System.Data/
%{_libdir}/mono/1.0/Novell.Directory.Ldap.dll
%{_libdir}/mono/gac/Novell.Directory.Ldap/
%{_libdir}/mono/1.0/System.DirectoryServices.dll
%{_libdir}/mono/gac/System.DirectoryServices/
%{_libdir}/mono/1.0/System.EnterpriseServices.dll
%{_libdir}/mono/gac/System.EnterpriseServices/

%files data-oracle
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/System.Data.OracleClient.dll
%{_libdir}/mono/gac/System.Data.OracleClient/

%files data-postgresql
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/Npgsql.dll
%{_libdir}/mono/gac/Npgsql/

%files data-sqlite
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/Mono.Data.SqliteClient.dll
%{_libdir}/mono/gac/Mono.Data.SqliteClient/

%files data-sybase
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/Mono.Data.SybaseClient.dll
%{_libdir}/mono/gac/Mono.Data.SybaseClient/

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/cert2spc.1*
%doc %{_mandir}/man1/cilc.1.gz
%doc %{_mandir}/man1/genxs.1*
%doc %{_mandir}/man1/ilasm.1*
%doc %{_mandir}/man1/makecert.1*
%doc %{_mandir}/man1/monoburg.1*
%doc %{_mandir}/man1/monodis.1*
%doc %{_mandir}/man1/monop.1*
%doc %{_mandir}/man1/monostyle.1.gz
%doc %{_mandir}/man1/oldmono.1.gz
%doc %{_mandir}/man1/secutil.1*
%doc %{_mandir}/man1/signcode.1*
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_bindir}/cilc*
%{_bindir}/gmcs
%{_bindir}/al*
%{_bindir}/cert2spc*
%{_bindir}/genxs*
%{_bindir}/ilasm*
%{_bindir}/makecert
%{_bindir}/MakeCert.exe
%{_bindir}/monodis*
%{_bindir}/monograph
%{_bindir}/monop*
%{_bindir}/monoresgen*
%{_bindir}/pedump
%{_bindir}/resgen
%{_bindir}/secutil*
%{_bindir}/signcode*
%dir %{_datadir}/mono/
%dir %{_datadir}/mono/*
%{_datadir}/mono/cil/cil-opcodes.xml
%dir %{_includedir}/mono/
%dir %{_includedir}/mono/*
%{_includedir}/mono/*/*.h
%{_includedir}/mono/cil/opcode.def
%{_libdir}/libmono-profiler-cov.*
%exclude %{_libdir}/libMonoPosixHelper.a
%exclude %{_libdir}/libMonoPosixHelper.la
%exclude %{_libdir}/libmint.a
%exclude %{_libdir}/libmint.la
%exclude %{_libdir}/libmono.a
%exclude %{_libdir}/libmono.la
%{_libdir}/mono/1.0/PEAPI.dll
%{_libdir}/mono/gac/PEAPI/
%{_libdir}/mono/2.0/gmcs.exe
%{_libdir}/mono/2.0/mscorlib.dll
%{_libdir}/mono/gac/Mono.Security.Win32/
%{_libdir}/mono/gac/nunit.core/
%{_libdir}/mono/gac/nunit.framework/
%{_libdir}/mono/gac/nunit.util/
%{_libdir}/pkgconfig/*.pc

%files extras
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/Microsoft.Vsa.dll
%{_libdir}/mono/gac/Microsoft.Vsa/
%{_libdir}/mono/1.0/System.Configuration.Install.dll
%{_libdir}/mono/gac/System.Configuration.Install/
%{_libdir}/mono/1.0/System.Management.dll
%{_libdir}/mono/gac/System.Management/
%{_libdir}/mono/1.0/System.Messaging.dll
%{_libdir}/mono/gac/System.Messaging/
%{_libdir}/mono/1.0/System.ServiceProcess.dll
%{_libdir}/mono/gac/System.ServiceProcess/

#%files ikvm
#%defattr(-, root, root, 0755)
#%{_libdir}/libmono-ikvm-jni.so*

%files locale-extras
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/I18N.MidEast.dll
%{_libdir}/mono/gac/I18N.MidEast/
%{_libdir}/mono/1.0/I18N.Rare.dll
%{_libdir}/mono/gac/I18N.Rare/
%{_libdir}/mono/1.0/I18N.CJK.dll
%{_libdir}/mono/gac/I18N.CJK/
%{_libdir}/mono/1.0/I18N.Other.dll
%{_libdir}/mono/gac/I18N.Other/

%files web
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/disco.1*
%doc %{_mandir}/man1/soapsuds.1*
%doc %{_mandir}/man1/wsdl.1*
%doc %{_mandir}/man1/xsd.1*
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_sysconfdir}/mono/browscap.ini
%{_sysconfdir}/mono/DefaultWsdlHelpGenerator.aspx
%{_bindir}/disco*
%{_bindir}/soapsuds*
%{_bindir}/wsdl*
%{_bindir}/xsd*
%{_libdir}/mono/1.0/Mono.Http.dll
%{_libdir}/mono/gac/Mono.Http/
%{_libdir}/mono/1.0/System.Runtime.Remoting.dll
%{_libdir}/mono/gac/System.Runtime.Remoting/
%{_libdir}/mono/1.0/System.Runtime.Serialization.Formatters.Soap.dll
%{_libdir}/mono/gac/System.Runtime.Serialization.Formatters.Soap/
%{_libdir}/mono/1.0/System.Web.dll
%{_libdir}/mono/gac/System.Web/
%{_libdir}/mono/1.0/System.Web.Services.dll
%{_libdir}/mono/gac/System.Web.Services/

%files winforms
%defattr(-, root, root, 0755)
%dir %{_libdir}/mono/
%dir %{_libdir}/mono/*
%{_libdir}/mono/1.0/Accessibility.dll
%{_libdir}/mono/gac/Accessibility/
%{_libdir}/mono/1.0/System.Design.dll
%{_libdir}/mono/gac/System.Design/
%{_libdir}/mono/1.0/System.Drawing.Design.dll
%{_libdir}/mono/gac/System.Drawing.Design/
%{_libdir}/mono/1.0/System.Windows.Forms.dll
%{_libdir}/mono/gac/System.Windows.Forms/

%files complete
%defattr(-, root, root, 0755)

%changelog
* Tue Feb 22 2005 Dag Wieers <dag@wieers.com> - 1.0.6-1
- Updated to release 1.0.6.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Fri Mar 19 2004 Dag Wieers <dag@wieers.com> - 0.31-0
- Updated to release 0.31.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.30.2-0
- Updated to release 0.30.2.

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.30.1-0
- Updated to release 0.30.1.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 0.29-0
- Updated to release 0.29.

* Sat Oct 04 2003 Dag Wieers <dag@wieers.com> - 0.28-0
- Updated to release 0.28.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.26-0
- Updated to release 0.26.

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 0.25-0
- Updated to release 0.25.

* Sun May 25 2003 Dag Wieers <dag@wieers.com> - 0.24-1
- Added Mono binfmt-support sysv script.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.24-0
- Updated to release 0.24.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 0.23-0
- Initial package. (using DAR)
