# $Id$
# Authority: dag
# Upstream:

%define real_name SING

Summary: Send ICMP nasty garbage
Name: sing
Version: 1.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sf.net/projects/sing/

Source: http://dl.sf.net/sing/SING-%{version}.tgz
Patch: sing-1.1-libnet-gcc32.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
SING stands for 'Send ICMP Nasty Garbage'. It is a tool that sends ICMP
packets fully customized from command line. Its main purpose is to replace
the ping command but adding certain enhancements (Fragmentation, spoofing,
...)

%prep
%setup -n %{real_name}-%{version}
%patch0

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Sun Apr 25 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
