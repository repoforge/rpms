# $Id$
# Authority: dag
# Upstream: Trey Harris <treyharris$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Commands-Guarded

Summary: Perl module that provides better scripts through guarded commands
Name: perl-Commands-Guarded
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Commands-Guarded/

Source: http://search.cpan.org/CPAN/authors/id/T/TR/TREY/Commands-Guarded-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-Commands-Guarded is a Perl module that provides better scripts
through guarded commands.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Commands::Guarded.3pm*
%dir %{perl_vendorlib}/Commands/
%{perl_vendorlib}/Commands/Guarded.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 1.01-1
- Updated to version 1.01.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
