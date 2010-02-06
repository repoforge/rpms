# $Id:$
# Upstream: Dave Rolsky <autarch@urth.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name File-ChangeNotify

Summary: Watch for changes to files, cross-platform style
Name: perl-File-ChangeNotify
Version: 0.12
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-ChangeNotify

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/File-ChangeNotify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Params::Validate) >= 0.08
BuildRequires: perl(MooseX::SemiAffordanceAccessor)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
Requires: perl(Carp)
Requires: perl(Class::MOP)
Requires: perl(File::Find)
Requires: perl(File::Spec)
Requires: perl(Module::Pluggable::Object)
Requires: perl(Moose)
Requires: perl(MooseX::Params::Validate) >= 0.08
Requires: perl(MooseX::SemiAffordanceAccessor)
Requires: perl(Time::HiRes)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module provides an API for creating a File::ChangeNotify::Watcher subclass that will work on your platform.

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
%doc MANIFEST README
%{perl_vendorlib}/File/ChangeNotify.pm
%{perl_vendorlib}/File/ChangeNotify/Event.pm
%{perl_vendorlib}/File/ChangeNotify/Watcher.pm
%{perl_vendorlib}/File/ChangeNotify/Watcher/Default.pm
%{perl_vendorlib}/File/ChangeNotify/Watcher/Inotify.pm
%{perl_vendorlib}/File/ChangeNotify/Watcher/KQueue.pm
%doc %{_mandir}/man3/File::ChangeNotify.3pm.gz
%doc %{_mandir}/man3/File::ChangeNotify::Event.3pm.gz
%doc %{_mandir}/man3/File::ChangeNotify::Watcher.3pm.gz
%doc %{_mandir}/man3/File::ChangeNotify::Watcher::Default.3pm.gz
%doc %{_mandir}/man3/File::ChangeNotify::Watcher::Inotify.3pm.gz
%doc %{_mandir}/man3/File::ChangeNotify::Watcher::KQueue.3pm.gz


%changelog
* Sat Feb 06 2010 Christoph Maser <cmr@financial.com> - 0.12-1
- initial package

