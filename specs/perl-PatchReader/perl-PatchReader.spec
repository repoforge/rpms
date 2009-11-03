# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PatchReader

Summary: Utilities to read and manipulate patches and CVS
Name: perl-PatchReader
Version: 0.9.5
Release: 2.2%{?dist}
License: MPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PatchReader/

Source: http://www.cpan.org/authors/id/J/JK/JKEISER/PatchReader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(File::Temp)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: cvs

%description
PatchReader is a set of utilities for reading in, transforming, and doing
various other things with a patch.  It basically allows you to create a
chain of readers that can read a patch, remove files from a patch, add
CVS context, fix up the patch root according to CVS, and output the patch
as raw unified or through a template processor (used in some places to
output a patch as HTML).

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
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/PatchReader.pm
%{perl_vendorlib}/PatchReader/

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.9.5-2
- Fixed group.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Initial package. (using DAR)
