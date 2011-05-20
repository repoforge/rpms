# $Id$
# Authority: shuff
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Filesys-Notify-Simple

Summary: Simple and dumb file system watcher
Name: perl-Filesys-Notify-Simple
Version: 0.07
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filesys-Notify-Simple/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Filesys-Notify-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Filter::Util::Call)
# Requires: perl(Linux::Inotify2)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Filesys::Notify::Simple is a simple but unified interface to get notifications
of changes to a given filesystem path. It utilizes inotify2 on Linux and
fsevents on OS X if they're installed, with a fallback to the full directory
scan if they're not available.

There are some limitations in this module. If you don't like it, use
File::ChangeNotify.

* There is no file name based filter. Do it in your own code.
* You can not get types of events (created, updated, deleted).
* Currently wait method blocks.

In return, this module doesn't depend on any non-core modules. Platform
specific optimizations with Linux::Inotify2 and Mac::FSEvents are truly
optional.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Filesys/Notify/Simple.pm
#%{perl_vendorlib}/Filesys/Notify/Simple/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri May 20 2011 Steve Huff <shuff@vecna.org> - 0.07-1
- Initial package.
