# $Id$
# Authority: dag
# Upstream: Florian Ragwitz <rafl@debian.org>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Devel

Summary: Catalyst Development Tools
Name: perl-Catalyst-Devel
Version: 1.26
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Devel/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Catalyst-Devel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Catalyst) >= 5.80014
BuildRequires: perl(Catalyst::Action::RenderView) >= 0.10
BuildRequires: perl(Catalyst::Plugin::ConfigLoader) >= 0.23
BuildRequires: perl(Catalyst::Plugin::Static::Simple) >= 0.28
BuildRequires: perl(Config::General) >= 2.42
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::ChangeNotify) >= 0.07
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(Module::Install) >= 0.91
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Emulate::Class::Accessor::Fast)
BuildRequires: perl(Path::Class) >= 0.09
BuildRequires: perl(Template) >= 2.14
#BuildRequires: perl(Test::More) >= 0.94
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(namespace::clean)
Requires: perl(Catalyst) >= 5.80014
Requires: perl(Catalyst::Action::RenderView) >= 0.10
Requires: perl(Catalyst::Plugin::ConfigLoader) >= 0.23
Requires: perl(Catalyst::Plugin::Static::Simple) >= 0.28
Requires: perl(Config::General) >= 2.42
Requires: perl(File::ChangeNotify) >= 0.07
Requires: perl(File::Copy::Recursive)
Requires: perl(File::ShareDir)
Requires: perl(Module::Install) >= 0.91
Requires: perl(Moose)
Requires: perl(MooseX::Emulate::Class::Accessor::Fast)
Requires: perl(Path::Class) >= 0.09
Requires: perl(Template) >= 2.14
Requires: perl(namespace::autoclean)
Requires: perl(namespace::clean)

%filter_from_requires /^perl*/d
%filter_setup

%description
Catalyst Development Tools.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/Catalyst::Devel.3pm*
%doc %{_mandir}/man3/Catalyst::Helper.3pm*
%doc %{_mandir}/man3/Catalyst::Restarter.3pm*
%doc %{_mandir}/man3/Catalyst::Restarter::Forking.3pm*
%doc %{_mandir}/man3/Catalyst::Restarter::Win32.3pm*
%doc %{_mandir}/man3/Module::Install::Catalyst.3pm*
%dir %{perl_vendorlib}/Catalyst/
#%{perl_vendorlib}/Catalyst/Devel/
%{perl_vendorlib}/Catalyst/Devel.pm
%{perl_vendorlib}/Catalyst/Helper.pm
%{perl_vendorlib}/Catalyst/Restarter.pm
%{perl_vendorlib}/Catalyst/Restarter/Forking.pm
%{perl_vendorlib}/Catalyst/Restarter/Win32.pm
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/Changes.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/Makefile.PL.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/README.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/lib/Helper/compclass.pm.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/lib/MyApp.pm.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/lib/MyApp/Controller/Root.pm.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/myapp.conf.tt
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/root/favicon.ico.bin
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/root/static/images/
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/root/static/images/catalyst_logo.png.bin
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/script/
%{perl_vendorlib}/auto/share/dist/Catalyst-Devel/t
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install/Catalyst.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.26-1
- Updated to version 1.26.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 1.06-1
- Updated to release 1.06.

* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
