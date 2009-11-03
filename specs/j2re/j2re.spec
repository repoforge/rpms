# $Id$
# Authority: dag


%{?fc2:%define _without_compat_xorg 1}
%{?fc1:%define _without_compat_xorg 1}
%{?el3:%define _without_compat_xorg 1}
%{?rh9:%define _without_compat_xorg 1}
%{?rh7:%define _without_compat_xorg 1}
%{?rh7:%define _without_gcc3 1}
%{?el2:%define _without_compat_xorg 1}
%{?el2:%define _without_gcc3 1}
%{?rh6:%define _without_gcc3 1}

%define real_version 1_4_2
%define real_release 06

Summary: Sun Java(tm) 2 Runtime Environment
Name: j2re
Version: 1.4.2
Release: 11%{?dist}
Group: Development/Languages
License: Redistributable, BCLA
URL: http://java.sun.com/j2se/1.4.2/download.html

Source: j2re-%{real_version}_%{real_release}-linux-i586.bin
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i586
AutoReq: no
BuildRequires: expect
Provides: j2re = %{version}, java = %{version}, j2re-java = %{version}
Obsoletes: kaffe, java < %{version}, j2re-java < %{version}
#Requires: shared-mime-info
%{!?_without_compat_xorg:Requires: xorg-x11-deprecated-libs}

%description
This packages provides the environment to run java 2 aplications with JRE.

%package -n mozilla-j2re
Summary: Sun Java(tm) 2 Plug-in for the mozilla browser
Group: Applications/Internet
Requires: j2re = %{version}
#Requires: %{_libdir}/mozilla/plugins/
Provides: java-plugin = %{version}, j2re-java-plugin = %{version}
Obsoletes: java-plugin < %{version}, j2re-java-plugin = < %{version}

%description -n mozilla-j2re
Sun Java(tm) 2 Plug-in for the mozilla browser.
This will enable Java applets be seen on browsers like
mozilla, galeon, netscape 4 and netscape 6.

%prep
%setup -c -T
%{__rm} -rf j2re%{version}_%{real_release}

%{__cat} <<'EOF' >java.sh
JREHOME="%{_libdir}/jre/lib/i386"
JAVAWSHOME="%{_libdir}/jre/javaws"
#LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$JREHOME:$JAVAWSHOME"
PATH="$PATH:%{_libdir}/jre/bin"
EOF

%{__cat} <<EOF >java.applications
java
	command=java -jar
	name=Java Runtime Engine
	can_open_multiple_files=false
	startup_notify=false
	expects_uris=false
	requires_terminal=false
	mime_types=application/x-java-archive

javaws
	command=javaws
	name=Java Web Start
	can_open_multiple_files=false
	startup_notify=false
	expects_uris=true
	requires_terminal=false
	mime_types=application/x-java-jnlp-file
EOF

%{__cat} <<EOF >java.desktop
[Desktop Entry]
Name=Java
Comment=Change system-wide Java settings
Icon=java.png
Exec=%{_libdir}/jre/bin/ControlPanel
Terminal=false
Type=Application
StartupNotify=false
MimeType=application/x-java-archive;application/x-jar;
Categories=Application;Settings;X-Red-Hat-Base;
EOF

%{__cat} <<EOF >java.mime
application/x-java-archive
	ext: jar

application/x-java-jnlp-file
	ext: jnlp
EOF

%{__cat} <<EOF >java.keys
application/x-jar
	description=Java Archive
	default_action_type=application
	default_application_id=java
	category=Software Development
	open=java -jar %f
	view=java -jar %f
	icon-filename=gnome-application-x-jar.png

application/x-java-archive
	description=Java Archive
	default_action_type=application
	default_application_id=java
	category=Software Development
	open=java -jar %f
	view=java -jar %f
	icon-filename=gnome-application-x-jar.png

application/x-java-jnlp-file
	description=Java Web Start Application
	default_action_type=application
	default_application_id=javaws
	category=Software Development
	open=javaws %f
	view=javaws %f
	icon-filename=java.png
EOF

%{__cat} <<EOF >java.xml
<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
	<mime-type type="application/x-jar">
		<comment>Java Archive</comment>
		<glob pattern="*.jar"/>
	</mime-type>
	<mime-type type="application/x-java-archive">
		<comment>Java Archive</comment>
		<glob pattern="*.jar"/>
	</mime-type>
	<mime-type type="application/x-java-jnlp-file">
		<comment>Java Web Start Application</comment>
		<glob pattern="*.jnlp"/>
	</mime-type>
</mime-info>
EOF

%build
expect -f- <<EOF
	set timeout -1
	spawn sh -x %{SOURCE0}
	match_max 100000
	send -- "\r"
	send -- "q"
	expect -exact "Do you agree to the above license terms? \[yes or no\] \r\n"
	send -- "yes\r"
	send -- "exit\r"
	expect eof
EOF
#%{__rm} -f %{SOURCE0}.run
#%{__perl} -pi.run -e 'if ($a != "exit 0") { print "a=[$_]";  $a=$_; $_=""; }' %{SOURCE0}
#chmod +x %{SOURCE0}.run
#%{SOURCE0}.run

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 java.sh %{buildroot}%{_sysconfdir}/profile.d/java.sh
%{__install} -Dp -m0644 java.applications %{buildroot}%{_datadir}/application-registry/java.applications
%{__install} -Dp -m0644 java.desktop %{buildroot}%{_datadir}/applications/java.desktop
%{__install} -Dp -m0644 java.mime %{buildroot}%{_datadir}/mime-info/java.mime
%{__install} -Dp -m0644 java.keys %{buildroot}%{_datadir}/mime-info/java.keys
%{__install} -Dp -m0644 java.xml %{buildroot}%{_datadir}/mime/packages/java.xml

cd j2re%{version}_%{real_release}

%{__install} -d -m0755 %{buildroot}%{_libdir}/jre/
%{__cp} -apv bin/ javaws/ lib/ plugin/ %{buildroot}%{_libdir}/jre/

%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__cp} -apv man/man1/* %{buildroot}%{_mandir}/man1/

%{__mv} -f CHANGES COPYRIGHT ControlPanel.html LICENSE README THIRDPARTYLICENSEREADME.txt Welcome.html ../

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f ../lib/jre/bin/java %{buildroot}%{_bindir}/
%{__ln_s} -f ../lib/jre/javaws/javaws %{buildroot}%{_bindir}/

%{__install} -Dp -m0644 plugin/desktop/sun_java.png %{buildroot}%{_datadir}/pixmaps/java.png

find %{buildroot}%{_libdir}/jre/ -type f -exec %{__chmod} 0644 {} \;
find %{buildroot}%{_libdir}/jre/bin/ -type f -exec %{__chmod} 0755 {} \;
find %{buildroot}%{_libdir}/jre/ -type f -name "*.so" -exec %{__chmod} 0755 {} \;

#find . -type f -exec %{__chmod} 0644 {} \;

%{__chmod} 0644 %{buildroot}%{_mandir}/man?/*
%{__chmod} 0755 %{buildroot}%{_libdir}/jre/javaws/javaws{,bin}

%{__install} -d -m0755 %{buildroot}%{_libdir}/mozilla/plugins/
%{!?_without_gcc3:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610-gcc32/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}
%{?_without_gcc3:%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns610/libjavaplugin_oji.so %{buildroot}%{_libdir}/mozilla/plugins/}

%{__install} -d -m0755 %{buildroot}%{_libdir}/netscape/plugins/
%{__ln_s} -f %{_libdir}/jre/plugin/i386/ns4/libjavaplugin.so %{buildroot}%{_libdir}/netscape/plugins/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_mandir}/man1/rmiregistry.1*

%post
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYRIGHT ControlPanel.html LICENSE README THIRDPARTYLICENSEREADME.txt Welcome.html
%doc %{_mandir}/man?/*
%dir %{_libdir}/jre/
%config %{_sysconfdir}/profile.d/java.sh
%{_bindir}/java
%{_bindir}/javaws
%{_datadir}/application-registry/java.applications
%{_datadir}/applications/java.desktop
%{_datadir}/mime-info/java.*
%{_datadir}/pixmaps/java.png
%{_datadir}/mime/packages/java.xml
%{_libdir}/jre/bin/
%{_libdir}/jre/lib/
%{_libdir}/jre/javaws/

%files -n mozilla-j2re
%defattr(-, root, root, 0755)
%{_libdir}/jre/plugin/
%{_libdir}/mozilla/plugins/libjavaplugin_oji.so
%{_libdir}/netscape/plugins/libjavaplugin.so

%changelog
* Wed Mar 02 2005 Dag Wieers <dag@wieers.com> - ??
- Added dependency to xorg-x11-deprecated-libs. (Jim Bartus)

* Thu Nov 25 2004 Dag Wieers <dag@wieers.com> - 1.4.2-11
- Updated to release 1_4_2_06.
- Made plugins executable. (Nils Toedtmann)

* Thu Nov 18 2004 Dag Wieers <dag@wieers.com> - 1.4.2-10
- Removed %%{_libdir}/mozilla/plugins/

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 1.4.2-9
- Removed mozilla dependency. (Anand Buddhdev)

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 1.4.2-8
- Don't fail when update-mime-database is missing. (David Vernon)

* Wed Jun 02 2004 Dag Wieers <dag@wieers.com> - 1.4.2-7
- Fixed java.sh. (Alexandre Oliva)

* Tue Jun 01 2004 Dag Wieers <dag@wieers.com> - 1.4.2-6
- Updated to release 1_4_2_04.
- Added desktop-entries, mime-types and symlinks. (Rivas Diaz)

* Wed Dec 10 2003 Dag Wieers <dag@wieers.com> - 1.4.2-5
- Updated to release 1_4_2_03.

* Tue Jul 22 2003 Dag Wieers <dag@wieers.com> - 1.4.2-4
- Fixed a silly permissions problem.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 1.4.2-3
- Updated release to 2 for compatibility reasons.
- Initial package. (using DAR)
