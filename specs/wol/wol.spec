# $Id$

# Authority: dag

Summary: The Wake On Lan client.
Name: wol
Version: 0.7.0
Release: 0
License: GPL
Group: Applications/Internet
URL: http://ahh.sf.net/wol/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ahh/wol-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
wol is the Wake On Lan client. It wakes up magic packet compliant machines
such as boxes with wake-on-lan ethernet-cards. Some workstations provides
SecureON which extends wake-on-lan with a password.
This feature is also provided by wol.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_infodir}/wol.*
%doc %{_mandir}/man?/*
%{_bindir}/*
#{_datadir}/locale/*/*/*

%changelog
* Thu Aug 21 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
