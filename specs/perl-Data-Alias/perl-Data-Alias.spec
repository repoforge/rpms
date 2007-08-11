# $Id$
# Authority: dries
# Upstream: Matthijs van Duin <xmath-no-spam$nospam,cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Alias

Summary: Comprehensive set of aliasing operations
Name: perl-Data-Alias
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Alias/

Source: http://search.cpan.org//CPAN/authors/id/X/XM/XMATH/Data-Alias-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.1

%description
Comprehensive set of aliasing operations.

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
%doc Changes README
%doc %{_mandir}/man3/Data::Alias*.3pm*
%dir %{perl_vendorarch}/Data/
%{perl_vendorarch}/Data/Alias.pm
%dir %{perl_vendorarch}/auto/Data/
%{perl_vendorarch}/auto/Data/Alias/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
