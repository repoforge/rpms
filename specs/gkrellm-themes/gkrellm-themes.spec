# $Id$
# Authority: matthias

Summary: Some themes for the GNU Krell Monitor
Name: gkrellm-themes
Version: 2.1.8
Release: 4%{?dist}
License: GPL
Group: Applications/System
Source: gkrellm-themes.tar.bz2
URL: http://muhri.net/gkrellm/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gkrellm >= 2.0.0
BuildRequires: /usr/bin/find
BuildArch: noarch

%description
GKrellM charts SMP CPU, load, Disk, and all active net interfaces
automatically. An on/off button and online timer for the PPP interface
is provided. Monitors for memory and swap usage, file system, internet
connections, APM laptop battery, mbox style mailboxes, and cpu temps.
Also includes an uptime monitor, a hostname label, and a clock/calendar.

This package contains various themes to use with GKrellM. You will of
course have to install the main GKrellM package to use them.

%prep
%setup -n %{name}


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}/gkrellm2/themes
cd %{buildroot}%{_datadir}/gkrellm2/themes
/usr/bin/find %{_builddir}/%{name} -name "*gz" -exec %{__tar} -xzvf {} \;
# Cleanup / Fixup
/usr/bin/find . -name ".xvpics" -o -name "CVS" -o -name "*~" | xargs %{__rm} -rf
/usr/bin/find . -type d -exec chmod 755 {} \;
/usr/bin/find . -type f -exec chmod 644 {} \;


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_datadir}/gkrellm2/themes/*


%changelog
* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 2.1.8-4
- Also prevent CVS and *~ files from being included.

* Wed Jan  7 2004 Matthias Saou <http://freshrpms.net/> 2.1.8-3
- Fix permissions for the installed files, thanks to Brett Pemberton.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.8-2
- Rebuild for Fedora Core 1.
- Not a single new skin on http://muhri.net/gkrellm/ :-(

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Added all the latest skins.

* Sat Jan 25 2003 Matthias Saou <http://freshrpms.net/>
- Added all the latest themes from muhri.net.

* Wed Oct  9 2002 Matthias Saou <http://freshrpms.net/>
- Added the great yummiyogurt theme still not on muhri.net.

* Thu Oct  3 2002 Matthias Saou <http://freshrpms.net/>
- Repackages *all* available themes from muhri.net.

* Mon Apr 30 2001 Matthias Saou <http://freshrpms.net/>
- Added some more themes.

* Sun Dec 31 2000 Matthias Saou <http://freshrpms.net/>
- Initial release with a few themes I like.

