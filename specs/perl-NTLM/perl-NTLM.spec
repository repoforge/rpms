# $Id$
# Authority: dries
# Upstream: Yee Man Chan <ymc$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name NTLM

Summary: Extension for NTLM related computations
Name: perl-NTLM
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/NTLM/

Source: http://search.cpan.org/CPAN/authors/id/B/BU/BUZZ/NTLM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Obsoletes: perl-Authen-NTLM

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Authen/NTLM.pm
%{perl_vendorlib}/Authen/NTLM/DES.pm
%{perl_vendorlib}/Authen/NTLM/MD4.pm
%{perl_vendorlib}/Authen/NTLM

%changelog
* Thu Jan  7 2010 Christoph Maser <cmr@financial.com> - 1.05-1
- Updated to version 1.05.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
