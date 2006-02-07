# $Id$
# Authority: dag
# Upstream: Eddy Vervest <eddy$clevervest,com>

Summary: HTTP based time synchronization tool
Name: htpdate
Version: 0.9.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.clevervest.com/htp/

Source: http://www.clevervest.com/htp/archive/c/htpdate-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /sbin/chkconfig

%description
The HTTP Time Protocol (HTP) is used to synchronize a computer's time with
web servers as reference time source. Htpdate will synchronize your computer's
time by extracting timestamps from HTTP headers found in web servers responses.
Htpdate can be used as a daemon, to keep your computer synchronized.

Accuracy of htpdate is usually better than 0.5 seconds (even better with
multiple servers). If this is not good enough for you, try the ntpd package.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 htpdate %{buildroot}%{_bindir}/htpdate
%{__install} -D -m0644 htpdate.8.gz %{buildroot}%{_mandir}/man8/htpdate.8.gz
%{__install} -D -m0755 scripts/htpdate.init %{buildroot}%{_initrddir}/htpdate

%post
/sbin/chkconfig --add htpdate

%preun
if [ $1 -eq 0 ]; then
	/sbin/service htpdate stop &>/dev/null || :
	/sbin/chkconfig --del htpdate
fi

%postun
/sbin/service htpdate condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README
%doc %{_mandir}/man8/htpdate.8*
%config %{_initrddir}/htpdate
%{_bindir}/htpdate

%changelog
* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Initial package. (using DAR)
