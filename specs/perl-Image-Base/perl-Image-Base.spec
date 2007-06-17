# $Id$

# Authority: dries
# Upstream: Mark Summerfield <summer$perlpress,com>

%define real_name Image-Base
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Base class for loading, manipulating and saving images
Name: perl-Image-Base
Version: 1.07
Release: 2.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Base/

Source: http://www.cpan.org/modules/by-module/Image/Image-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module contains a base class for loading, manipulating and saving images.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Image/Base.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-2.2
- Rebuild for Fedora Core 5.

* Tue Oct 05 2004 Dries Verachtert <dries@ulyssis.org> - 1.07-2
- Rebuild.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Initial package.
