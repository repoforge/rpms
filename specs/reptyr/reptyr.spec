# $Id$
# Authority: shuff
# Upstream: Nelson Elhage <nelhage$ksplice,com>

%define github_hash g3cad834
%define tarball_hash b83e8f6

Summary: Reparent a running program to a new terminal
Name: reptyr
Version: 0.3
Release: 1%{?dist}
License: MIT
Group: Applications/Utilities
URL: https://github.com/nelhage/reptyr/

Source: https://download.github.com/nelhage-reptyr-reptyr-%{version}-0-%{github_hash}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Buildarch: noarch
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge

%description
reptyr is a utility for taking an existing running program and attaching it to
a new terminal. Started a long-running process over ssh, but have to leave and
don't want to interrupt it? Just start a screen, use reptyr to grab it, and
then kill the ssh session and head on home.

%prep
%setup -n nelhage-reptyr-%{tarball_hash}

# fix hardcoded prefix in Makefile
%{__perl} -pi -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|;' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog NOTES README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Jun 01 2011 Steve Huff <shuff@vecna.org> - 0.3-1
- Initial package.
