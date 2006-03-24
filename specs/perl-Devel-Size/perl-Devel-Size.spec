# $Id$
# Authority: dries
# Upstream: Dan Sugalski <dan$sidhe,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Size

Summary: Find the memory usage of perl variables
Name: perl-Devel-Size
Version: 0.64
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Size/

Source: http://search.cpan.org/CPAN/authors/id/D/DS/DSUGAL/Devel-Size-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl extension for finding the memory usage of Perl variables.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Devel/Size.pm
#%{perl_vendorarch}/Devel/Size/
%{perl_vendorarch}/auto/Devel/Size/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1.2
- Rebuild for Fedora Core 5.

* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 0.64-1
- Initial package.
