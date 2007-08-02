# $Id$
# Authority: dries
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Format-Builder

Summary: Create DateTime parser classes and objects
Name: perl-DateTime-Format-Builder
Version: 0.7807
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Format-Builder/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-Format-Builder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Module::Build)

%description
With this module, you can create DateTime parser classes and objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DateTime/Format/Builder.p*
%{perl_vendorlib}/DateTime/Format/Builder/

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.7807-1
- Updated to release 0.7807.

* Sun Dec 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.7806-1
- Initial package.
