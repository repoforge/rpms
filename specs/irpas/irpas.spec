# $Id$
# Authority: dag
# Upstream: FX <fx$phenoelit,de>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Inter-network routing protocol attack suite
Name: irpas
Version: 0.10
Release: 1.2%{?dist}
License: distributable
Group: Applications/Internet
URL: http://www.phenoelit.de/irpas/

Source: http://www.phenoelit.de/irpas/irpas_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Routing protocols are by definition protocols, which are used by routers
to communicate with each other about ways to deliver routed protocols,
such as IP. While many improvements have been done to the host security
since the early days of the Internet, the core of this network still uses
unauthenticated services for critical communication. Because most of the
routers you will see in todays environments are Cisco products, we focus
our work on these, which does not mean that it dosn't apply to other
router vendors.

The idea is to implement small tools which can be scripted for larger
tests while using the protocols describd in standards or white papers.
IRPAS is not a collection of exploits. While several circumstances can
lead to a denail of service attack, the tools try to implement routing
protocol functionality as described by the papers, therefore enabling
the user of these tools (probably you) to design it's own customized
attack.

%prep
%setup -c

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
