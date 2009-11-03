# $Id$
# Authority: dries
# Upstream: William R Ward <wrw$bayview,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Number-Format
%define real_version 1.72

Summary: Convert numbers to strings with pretty formatting
Name: perl-Number-Format
Version: 1.72a
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Number-Format/

Source: http://www.cpan.org/modules/by-module/Number/Number-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Number::Format is a library for formatting numbers.  Functions are
provided for converting numbers to strings in a variety of ways, and to
convert strings that contain numbers back into numeric form.  The output
formats may include thousands separators - characters inserted between
each group of three characters counting right to left from the decimal
point.  The characters used for the decimal point and the thousands
separator come from the locale information or can be specified by the
user.

%prep
%setup -n %{real_name}-%{real_version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Number/Format.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.72a-1
- Updated to version 1.72a.

* Sat Sep 23 2006 Dries Verachtert <dries@ulyssis.org> - 1.52-1
- Updated to release 1.52.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.51-1
- Updated to release 1.51.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.45-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.45-1
- Initial package.
