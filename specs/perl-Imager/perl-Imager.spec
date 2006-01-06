# $Id$
# Authority: dries
# Upstream: Tony Cook <tony$develop-help,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Imager

Summary: Extension for generating 24 bit images
Name: perl-Imager
Version: 0.47
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Imager/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TONYC/Imager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, libpng-devel, pkgconfig, freetype-devel, libungif-devel, libtiff-devel
BuildRequires: libjpeg-devel

%description
Perl extension for Generating 24 bit Images.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Imager.pm
%{perl_vendorarch}/Imager/
%{perl_vendorarch}/auto/Imager/

%changelog
* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Initial package.
