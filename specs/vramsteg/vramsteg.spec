# $Id$
# Authority: shuff
# Upstream: TaskWarrior <support$taskwarrior,org>

Summary: Text-based progress bars
Name: vramsteg
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://tasktools.org/projects/vramsteg.html

Source: http://www.vecna.org/fink/vramsteg-%{version}.tar.gz
Patch0: vramsteg_demo_paths.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: rpm-macros-rpmforge

%description
Vramsteg adds progress-bar capability to a script/program that otherwise does
not have one. If a program has a lengthy iterative operation, it may benefit
from using vramsteg, which provides these features:

* Display, removes or leaves a progress bar on screen
* Allows an arbitrary range to be represented (1-10, or 34-52, or 1-1000000)
* Has color, monochrome, or colorless progress bars
* Can display elapsed time
* Can estimate remaining time
* Configurable bar width
* Can show a prefix label
* Can show percentage completion

%prep
%setup
%patch0 -p1

%build
%{cmake}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix the docdir
%{__mv} %{buildroot}%{_docdir}/vramsteg %{buildroot}%{_docdir}/vramsteg-%{version}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL LICENSE NEWS README demo/ examples/
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Fri Aug  4 2012 Steve Huff <shuff@vecna.org> - 1.0.0-1
- Initial package.
