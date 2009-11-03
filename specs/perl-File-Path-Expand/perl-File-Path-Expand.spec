# $Id$
# Authority: dag
# Upstream: Richard Clamp <richardc$unixbeard,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Path-Expand

Summary: Expand filenames
Name: perl-File-Path-Expand
Version: 1.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Path-Expand/

Source: http://www.cpan.org/modules/by-module/File/File-Path-Expand-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Expand filenames.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/File::Path::Expand.3pm*
%dir %{perl_vendorlib}/File/
%dir %{perl_vendorlib}/File/Path/
#%{perl_vendorlib}/File/Path/Expand/
%{perl_vendorlib}/File/Path/Expand.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
