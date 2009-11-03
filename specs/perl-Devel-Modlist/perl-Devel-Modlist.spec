# $Id$
# Authority: dries
# Upstream: Randy J. Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Modlist

Summary: Collect a list of modules loaded at compile-time
Name: perl-Devel-Modlist
Version: 0.801
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Modlist/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-Modlist-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker), perl(Module::Build)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
Devel::Modlist is a small tool that emits a list of files that were brought
into a script via 'require' or 'use'. It lists these to the STDOUT descriptor
at the end of the script's run. Each file is converted to class-like name,
e.g. IO/File.pm is displayed as IO::File, and the version number, if found,
is displayed. Files ending in .al (auto-loading routines) and .ix (indices
for auto-loading) are ignored. Optionally, one can request that files in
the Perl core library area not be listed (see the manual page).

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
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Devel::Modlist.3pm*
%dir %{perl_vendorlib}/Devel/
#%{perl_vendorlib}/Devel/Modlist/
%{perl_vendorlib}/Devel/Modlist.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.801-1
- Updated to release 0.801.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 0.71-1
- Updated to release 0.71.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
