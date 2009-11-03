# $Id$
# Authority: dries
# Upstream: David A, Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-chdir

Summary: More sensible way to change directories
Name: perl-File-chdir
Version: 0.1002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-chdir/

Source: http://www.cpan.org/modules/by-module/File/File-chdir-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A more sensible way to change directories.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes INSTALL LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/File::chdir.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/chdir/
%{perl_vendorlib}/File/chdir.pm
%{perl_vendorlib}/File/chdir.pod

%changelog
* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.1002-1
- Updated to release 0.1002.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
