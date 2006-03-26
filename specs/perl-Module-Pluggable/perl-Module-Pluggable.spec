# $Id$
# Authority: dries
# Upstream: Simon Wistow <simon$thegestalt,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Pluggable

Summary: Automatically give your module the ability to have plugins
Name: perl-Module-Pluggable
Version: 2.97
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Pluggable/

Source: http://search.cpan.org/CPAN/authors/id/S/SI/SIMONW/Module-Pluggable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Provides a simple but, hopefully, extensible way of having 'plugins' for
your module. 

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Module/Pluggable.pm

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.97-1
- Updated to release 2.97.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.96-1.2
- Rebuild for Fedora Core 5.

* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 2.96-1
- Initial package.
