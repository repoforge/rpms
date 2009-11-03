# $Id$
# Authority: dries
# Upstream: Mark Jason Dominus (e*Pae**ae?(R)) (=Mark Jason Dominus) <mjd$plover,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Trace

Summary: Trace perl programs
Name: perl-Devel-Trace
Version: 0.10
Release: 1.2%{?dist}
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Trace/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Trace-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
If you run your program with "perl -d:Trace program", this module will
print a message to standard error just before each line is executed, like
the "-x" option of bash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Devel/Trace/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Devel/Trace.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1.2
- Rebuild for Fedora Core 5.

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Initial package.
