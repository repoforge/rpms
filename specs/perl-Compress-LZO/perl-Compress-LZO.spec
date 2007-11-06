# $Id$
# Authority: dries
# Upstream: Markus F.X.J. Oberhumer <cpan$oberhumer,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Compress-LZO

Summary: Bindings for LZO
Name: perl-Compress-LZO
Version: 1.08
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Compress-LZO/

Source: http://search.cpan.org/CPAN/authors/id/M/MF/MFX/Compress-LZO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), lzo-devel

%description
Perl-LZO provides LZO bindings for Perl, i.e. you can access the
LZO library from your Perl scripts thereby compressing ordinary
Perl strings.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Compress/
%{perl_vendorarch}/Compress/LZO.pm
%dir %{perl_vendorarch}/auto/Compress/
%{perl_vendorarch}/auto/Compress/LZO/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
