# $Id$
# Authority: dries
# Upstream: Mark Summerfield <summer$perlpress,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Xbm

Summary: Load, create, manipulate and save xbm image files
Name: perl-Image-Xbm
Version: 1.08
Release: 2.2
License: LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Xbm/

Source: http://www.cpan.org/modules/by-module/Image/Image-Xbm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can load, create, manipulate and save xbm image files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
                %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Image/Xbm.pm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-2.2
- Rebuild for Fedora Core 5.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Fixed the license (Thanks to David Necas !)

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
