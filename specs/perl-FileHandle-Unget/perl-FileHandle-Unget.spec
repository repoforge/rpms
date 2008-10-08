# $Id$
# Authority: dag
# Upstream: David Coppit <david$coppit,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FileHandle-Unget

Summary: FileHandle which supports multi-byte unget
Name: perl-FileHandle-Unget
Version: 0.1622
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FileHandle-Unget/

Source: http://www.cpan.org/modules/by-module/FileHandle/FileHandle-Unget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(Test::More)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(ExtUtils::MakeMaker::bytes)
BuildRequires: perl(Scalar::Util) >= 1.14
Requires: perl >= 0:5.00503

%description
FileHandle::Unget implements a filehandle which supports multi-byte unget.

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
%doc CHANGES LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/FileHandle::Unget.3pm*
%dir %{perl_vendorlib}/FileHandle/
%{perl_vendorlib}/FileHandle/Unget.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.1622-1
- Updated to release 0.1622.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.1621-1
- Initial package. (using DAR)
