# $Id$
# Authority: dag
# Upstream: Neil Neely <neil$neely,cx>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Serializer

Summary: Modules that serialize data structures
Name: perl-Data-Serializer
Version: 0.46
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Serializer/

Source: http://www.cpan.org/modules/by-module/Data/Data-Serializer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(AutoSplit)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)

%description
Modules that serialize data structures.

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
%doc Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/Data::Serializer.3pm*
%doc %{_mandir}/man3/Data::Serializer::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/Serializer/
%{perl_vendorlib}/Data/Serializer.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.43-1
- Updated to release 0.43.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.42-1
- Initial package. (using DAR)
