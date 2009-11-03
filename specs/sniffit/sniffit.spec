# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define real_version 0.3.7.beta

Summary: network protocol analyzer
Name: sniffit
Version: 0.3.7
Release: 0.beta.2%{?dist}
License: Freely distributable
Group: Applications/Internet
URL: http://reptile.rug.ac.be/~coder/sniffit/sniffit.html

Source: http://reptile.rug.ac.be/~coder/sniffit/files/%{name}.%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

Excludearch: ia64

%description
Sniffit is a robust non-commercial network protocol analyzer or packet
sniffer.  A packet sniffer basically listens to network traffic and
produces analysis based on the traffic and/or translates packets into
some level of human readable form.

%prep
%setup -n %{name}.%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sniffit   %{buildroot}%{_sbindir}/sniffit
%{__install} -Dp -m0644 sniffit.5 %{buildroot}%{_mandir}/man5/sniffit.5
%{__install} -Dp -m0644 sniffit.8 %{buildroot}%{_mandir}/man8/sniffit.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BETA-TESTING HISTORY LICENSE README.FIRST sample_config_file sniffit-FAQ
%doc %{_mandir}/man5/sniffit.5
%doc %{_mandir}/man8/sniffit.8
%{_sbindir}/sniffit

%changelog
* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.3.7-0.beta
- Initial package. (using DAR)
