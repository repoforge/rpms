# $Id$
# Authority: dag
# Upstream: Stéphane Bortzmeyer <bortz$users,sf,net>

Summary: Test performances of a remote host by sending it TCP "echo" packets
Name: echoping
Version: 5.2.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://echoping.sourceforge.net/

Source: http://dl.sf.net/echoping/echoping-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libidn-devel

%description
echoping is a small program to test (approximatively) performances of
a remote host by sending it TCP "echo" (or other protocol) packets.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING DETAILS INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.2.0-1.2
- Rebuild for Fedora Core 5.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 5.2.0-1
- Initial package. (using DAR)
