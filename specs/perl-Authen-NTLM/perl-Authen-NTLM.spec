# $Id$
# Authority: dries
# Upstream: Yee Man Chan <ymc$yahoo,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-NTLM

Summary: Extension for NTLM related computations
Name: perl-Authen-NTLM
Version: 0.31
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-NTLM/

Source: http://search.cpan.org/CPAN/authors/id/U/UM/UMVUE/Authen-NTLM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The NTLM (Windows NT LAN Manager) authentication scheme is the
authentication algorithm used by Microsoft.

NTLM authentication scheme is used in DCOM and HTTP environment. It is
used to authenticate DCE RPC packets in DCOM. It is also used to
authenticate HTTP packets to MS Web Proxy or MS Web Server.

Currently, it is the authentication scheme Internet Explorer chooses to
authenticate itself to proxies/web servers that supports NTLM.

As of this version, NTLM module only provides the client side functions
to calculate NT response and LM response. The next revision will provide
the server side functions that computes the nonce and verify the NTLM
responses.
	
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Authen/NTLM.pm
%{perl_vendorlib}/Authen/NTLM

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.31-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
