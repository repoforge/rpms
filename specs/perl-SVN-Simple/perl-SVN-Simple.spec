# $Id$
# Authority: dries
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Simple

Summary: Simple interface for delta editors
Name: perl-SVN-Simple
Version: 0.27
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Simple/

Source: http://www.cpan.org/modules/by-module/SVN/SVN-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, subversion-perl

%description
SVN::Simple is a simple interface to subversion's editor interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Simple/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.27-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Sun Nov 14 2004 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
