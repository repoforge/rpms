# $Id$
# Authority: dag

# BuildAsRoot: 1

%{?dist: %{expand: %%define %dist 1}}

%define real_version 1_4_2
%define real_release 03

Summary: Sun Java(tm) 2 Runtime Environment
Name: j2re
Version: 1.4.2
Release: 5
Group: Development/Languages
License: Redistributable, BCLA
URL: http://java.sun.com/j2se/1.4.2/download.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}-%{real_version}_%{real_release}-linux-i586.bin
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i586
AutoReq: no
BuildRequires: expect
Provides: %{name} = %{version}, java = %{version}, j2re-java = %{version}
Obsoletes: kaffe

%description
This packages provides the environment to run java 2 aplications with JRE.

%package -n mozilla-j2re
Summary: Sun Java(tm) 2 Plug-in for the mozilla browser
Group: Applications/Internet
Requires: %{name} = %{version}-%{release}, mozilla

Provides: java-plugin = %{version}, j2re-java-plugin = %{version}

%description -n mozilla-j2re
Sun Java(tm) 2 Plug-in for the mozilla browser.
This will enable Java applets be seen on browsers like
mozilla, galeon, netscape 4 and netscape 6.

%prep
%setup -c -T
%{__rm} -rf j2re%{version}_%{real_release}
expect -f- <<EOF
	set timeout -1
	spawn sh %{SOURCE0}
	match_max 100000
	send -- "\r"
	send -- "q"
	expect -exact "Do you agree to the above license terms? \[yes or no\] \r\n"
	send -- "yes\r"
	send -- "exit\r"
	expect eof
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/jre/ \
			%{buildroot}%{_mandir}/man1/ \
			%{buildroot}%{_libdir}/mozilla/plugins \
			%{buildroot}%{_libdir}/netscape/plugins

cd %{name}%{version}_%{real_release}
%{__cp} -av bin/ lib/ plugin/ %{buildroot}%{_libdir}/jre/
%{__cp} -av man/man1/* %{buildroot}%{_mandir}/man1/
%{__mv} -f CHANGES COPYRIGHT ControlPanel.html LICENSE README THIRDPARTYLICENSEREADME.txt Welcome.html ../

find %{buildroot}%{_libdir}/jre/ -type f -exec chmod 0644 {} \;
find %{buildroot}%{_libdir}/jre/bin/ -type f -exec chmod 0755 {} \;
chmod 0644 %{buildroot}%{_mandir}/man?/*
find . -type f -exec chmod 0644 {} \;

%{?fc2:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?fc1:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?el3:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh9:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh8:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh7:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?el2:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?rh6:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns4/libjavaplugin.so %{buildroot}%{_libdir}/netscape/plugins/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_mandir}/man1/rmiregistry.1*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT ControlPanel.html LICENSE README THIRDPARTYLICENSEREADME.txt Welcome.html 
%doc %{_mandir}/man?/*
# {_bindir}/*
%dir %{_libdir}/jre/
%{_libdir}/jre/bin/
%{_libdir}/jre/lib/

%files -n mozilla-j2re
%defattr(-, root, root, 0755)
%{_libdir}/jre/plugin/
%{_libdir}/mozilla/plugins/*
%{_libdir}/netscape/plugins/*

%changelog
* Wed Dec 10 2003 Dag Wieers <dag@wieers.com> - 1.4.2-5
- Updated to release 1_4_2_03.

* Tue Jul 22 2003 Dag Wieers <dag@wieers.com> - 1.4.2-4
- Fixed a silly permissions problem.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 1.4.2-3
- Updated release to 2 for compatibility reasons.
- Initial package. (using DAR)
