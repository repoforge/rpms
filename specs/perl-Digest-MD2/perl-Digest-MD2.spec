# $Id$

# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>


%define real_name Digest-MD2
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Interface to the MD2 algorithm
Name: perl-Digest-MD2
Version: 2.03
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-MD2/

Source: http://www.cpan.org/modules/by-module/Digest/Digest-MD2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The Digest::MD2 module allows you to use the RSA Data Security
Inc. MD2 Message Digest algorithm from within Perl programs.  The
algorithm takes as input a message of arbitrary length and produces as
output a 128-bit "fingerprint" or "message digest" of the input.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/Digest::MD2*
%{perl_vendorarch}/Digest/MD2.pm
%dir %{perl_vendorarch}/auto/Digest/
%dir %{perl_vendorarch}/auto/Digest/MD2/
%{perl_vendorarch}/auto/Digest/MD2/MD2.bs
%{perl_vendorarch}/auto/Digest/MD2/MD2.so

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.03-2
- Cleanup

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.03-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 2.03-1
- Initial package.
