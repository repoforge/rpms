# $Id$
# Authority: dag

Summary: HTTP regression testing and benchmarking utility
Name: siege
Version: 2.66
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.joedog.org/JoeDog/Siege/

Source: ftp://ftp.joedog.org/pub/siege/siege-%{version}.tar.gz
Patch0: siege-2.65-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel

%description
Siege is an http regression testing and benchmarking utility. 
It was designed to let web developers measure the performance of their code 
under duress, to see how it will stand up to load on the internet. 
Siege supports basic authentication, cookies, HTTP and HTTPS protocols. 
It allows the user hit a web server with a configurable number of concurrent 
simulated users. Those users place the webserver "under siege."

%prep
%setup
%patch0 -p1 -b .good

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 doc/urls.txt %{buildroot}%{_sysconfdir}/urls.txt

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING KNOWNBUGS MACHINES NEWS PLATFORM README*
%doc %{_mandir}/man1/bombardment.1*
%doc %{_mandir}/man1/siege.1*
%doc %{_mandir}/man1/siege.config*
%doc %{_mandir}/man1/siege2csv.1*
%doc %{_mandir}/man5/urls_txt.5*
%doc %{_mandir}/man7/layingsiege.7*
%config(noreplace) %{_sysconfdir}/urls.txt
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege.config
%{_bindir}/siege2csv.pl

%changelog
* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 2.66-1
- Initial package. (using DAR)
