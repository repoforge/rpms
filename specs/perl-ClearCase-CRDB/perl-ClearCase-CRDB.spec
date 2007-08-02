# $Id$
# Authority: dries
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name ClearCase-CRDB

Summary: Impact analysis in a clearmake build environment
Name: perl-ClearCase-CRDB
Version: 0.12
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ClearCase-CRDB/

Source: http://search.cpan.org/CPAN/authors/id/D/DS/DSB/ClearCase-CRDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Whouses provides a limited form of "impact analysis" in a clearmake
build environment. This is different from traditional impact analysis
In particular, it operates at the granularity of files rather than language
elements.

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
%doc %{_mandir}/man1/*
%{_bindir}/whouses
%{perl_vendorlib}/ClearCase/CRDB.pm
%{perl_vendorlib}/ClearCase/CRDB/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
