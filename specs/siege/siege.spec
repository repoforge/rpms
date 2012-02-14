# $Id$
# Authority: dag

Summary: HTTP regression testing and benchmarking utility
Name: siege
Version: 2.71
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.joedog.org/JoeDog/Siege/

Source: http://www.joedog.org/pub/siege/siege-%{version}.tar.gz
Patch0: siege-2.69-good.patch
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

# better default for log file (Bug 644631)
sed -i.orig doc/siegerc.in -e 's/^# logfile = *$/logfile = ${HOME}\/siege.log/'

%build

%configure --sysconfdir=/etc/siege
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# Create /etc/siege/urls.txt
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/siege
install -m 644 doc/urls.txt $RPM_BUILD_ROOT%{_sysconfdir}/siege/
# Create /etc/siege/siegerc
install -m 644 doc/siegerc $RPM_BUILD_ROOT%{_sysconfdir}/siege/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config(noreplace) %{_sysconfdir}/siege/siegerc
%config(noreplace) %{_sysconfdir}/siege/urls.txt
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/bombardment.1*
%doc %{_mandir}/man1/siege.1*
%doc %{_mandir}/man1/siege.config*
%doc %{_mandir}/man1/siege2csv.1*
%doc %{_mandir}/man5/urls_txt.5*
%doc %{_mandir}/man7/layingsiege.7*
%doc AUTHORS ChangeLog COPYING KNOWNBUGS MACHINES NEWS PLATFORM README*
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege.config
%{_bindir}/siege2csv.pl

%changelog
* Tue Feb 14 2012 David Hrbáč <david@hrbac.cz> - 2.71-1
- new upstream release

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 2.66-1
- Initial package. (using DAR)
