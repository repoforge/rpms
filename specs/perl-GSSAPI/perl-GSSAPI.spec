# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name GSSAPI

Summary: Perl extension providing access to the GSSAPIv2 library
Name: perl-GSSAPI
Version: 0.21
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/GSSAPI/

Source: http://www.cpan.org/authors/id/A/AG/AGROLMS/GSSAPI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(Test::Pod) >= 1.00, perl(Test::Pod::Coverage) >= 1.04
BuildRequires: krb5-devel

%description
This module gives access to the routines of the GSSAPI library, as
described in rfc2743 and rfc2744 and implemented by the Kerberos-1.2
distribution from MIT.

%prep
%setup -n GSSAPI-%{version}
chmod a-x examples/*.pl

%build
if pkg-config openssl; then
        export CFLAGS="%{optflags} $(pkg-config --cflags openssl)"
        export CPPFLAGS="%{optflags} $(pkg-config --cflags openssl)"
        export LDFLAGS="$(pkg-config --libs-only-L openssl)"
fi
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README examples/
%doc %{_mandir}/man3/*.3*
%{perl_vendorarch}/GSSAPI.pm
%{perl_vendorarch}/GSSAPI/
%{perl_vendorarch}/auto/GSSAPI/

%changelog
* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
