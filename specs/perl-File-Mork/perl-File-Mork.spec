# $Id$
# Authority: dag
# Upstream: Simon Wistow <simonw$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Mork

Summary: Perl module to read Mozilla URL history files
Name: perl-File-Mork
Version: 0.3
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Mork/

Source: http://www.cpan.org/modules/by-module/File/File-Mork-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-File-Mork is a Perl module to read Mozilla URL history files.

%package -n mork
Summary: Tool for dumping Mozilla URL history files
Group: Applications/File

Requires: %{name} = %{version}-%{release}

%description -n mork
mork is a tool for dumping Mozilla URL history files.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml examples/
%doc %{_mandir}/man3/File::Mork.3pm*
%dir %{perl_vendorlib}/File/
#%{perl_vendorlib}/File/Mork/
%{perl_vendorlib}/File/Mork.pm

%files -n mork
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/mork.1*
%{_bindir}/mork

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
