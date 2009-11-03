# $Id$
# Authority: dag
# Upstream: Bertrand Demiddelaer <bert$zehc,net>

Summary: Merges httpd log files by date
Name: mergelog
Version: 4.5
Release: 2%{?dist}
License: GPL
Group: Applications/File
URL: http://mergelog.sourceforge.net/

Source: http://dl.sf.net/mergelog/mergelog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel

%description
mergelog is a small and fast C program which merges by date httpd log
files in 'Common Log Format' from web servers behind round-robin DNS.
It has been designed to easily manage huge log files from highly
stressed servers. mergelog is distributed with zmergelog which supports
gzipped log files

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/mergelog.1*
%doc %{_mandir}/man1/zmergelog.1*
%{_bindir}/mergelog
%{_bindir}/zmergelog

%changelog
* Mon May  8 2006 Matthias Saou <http://freshrpms.net/> 4.5-2
- Add missing zlib-devel build requirement.
- Remove generic INSTALL file from docs.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 4.5-1
- Initial package. (using DAR)
