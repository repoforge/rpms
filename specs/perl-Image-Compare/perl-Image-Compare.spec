# $Id$
# Authority: dries
# Upstream: Avi Finkel <avi$finkel,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Compare

Summary: Compare two images in a variety of ways
Name: perl-Image-Compare
Version: 0.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Compare/

Source: http://search.cpan.org//CPAN/authors/id/A/AV/AVIF/Image-Compare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Regexp::Common), perl(Imager), perl(LWP)

%description
Image::Compare is a module for performing comparisons of images.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Image/Compare.pm

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
