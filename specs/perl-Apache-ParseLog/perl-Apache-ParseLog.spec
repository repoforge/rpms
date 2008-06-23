# $Id$
# Authority: dries
# Upstream: Akira Hangai <akira$hangai,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-ParseLog

Summary: Object-oriented Perl extension for parsing Apache log files
Name: perl-Apache-ParseLog
Version: 1.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-ParseLog/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-ParseLog-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Apache::ParseLog provides an easy way to parse the Apache log files,
using an object-oriented constructs. The data obtained using this
module are generic enough that it is flexible to use the data for
your own applications, such as CGI, simple text-only report generater,
feeding RDBMS, data for Perl/Tk-based GUI application, etc.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Apache/ParseLog.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
