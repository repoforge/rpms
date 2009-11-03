# $Id$
# Authority: dag
# Upstream: José Ignacio Sánchez Martín <topolb@users.sourceforge.net>


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Analyzing WEP encryption security on wireless networks
Name: weplab
Version: 0.1.5
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://weplab.sourceforge.net/

Source: http://dl.sf.net/weplab/weplab-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpcap, autoconf, automake
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
WepLab is a tool designed to teach how WEP works, what different
vulnerabilities it has, and how they can be used in practice to
break a WEP protected wireless network. So far, WepLab more than
a Wep Key Cracker, is a Wep Security Analyzer designed from an
educational point of view. The author has tried to leave the
source code as clear as possible, running away from optimizations
that would obfuscate it.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/weplab.1*
%{_bindir}/weplab

%changelog
* Thu Jul 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.5-1
- Update to release 0.1.5.

* Sun May 08 2005 Dag Wieers <dag@wieers.com> - 0.1.4-1
- Initial package. (using DAR)
