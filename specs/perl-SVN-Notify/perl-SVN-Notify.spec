# $Id$
# Authority: cmr
# Upstream: David E, Wheeler <david$kineticode,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Notify

Summary: Subversion activity notification
Name: perl-SVN-Notify
Version: 2.80
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Notify/

Source: http://search.cpan.org/CPAN/authors/id/D/DW/DWHEELER/SVN-Notify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long) >= 2.34
BuildRequires: perl(Module::Build) >= 0.2701
BuildRequires: perl(Test::More) >= 0.17
BuildRequires: perl >= 5.006
Requires: perl(Getopt::Long) >= 2.34
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup

%description
Subversion activity notification.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

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
%doc %{_mandir}/man3/SVN::Notify*.3pm*
%doc %{_mandir}/man1/svnnotify.1.gz
%{_bindir}/svnnotify
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Notify/
%{perl_vendorlib}/SVN/Notify.pm


%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 2.80-1
- Updated to version 2.80.

* Fri Jun 12 2009 Unknown - 2.79-1
- Initial package. (using DAR)
