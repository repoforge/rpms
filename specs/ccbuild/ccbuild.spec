# $Id$
# Authority: dries
# Upstream: A. Bram Neijt <bneijt$gmail,com>

Summary: Dynamic makefiles
Name: ccbuild
Version: 1.5.4
Release: 2%{?dist}
License: GPL
Group: Development/Tools
URL: http://ccbuild.sourceforge.net/

Source: http://dl.sf.net/ccbuild/ccbuild-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, flex

%description
ccbuild is like a dynamic Makefile. ccbuild finds all programs in the
current directory (containing "int main") and builds them. For this,
it reads the C++ sources and looks at all local and global includes.
All C++ files surrounding local includes are considered objects for
the main program. The global includes lead to extra compiler
arguments using a configuration file. ccbuild splits these arguments
for compilation and linking, keeping the linking arguments back for
later use. It should allow development without any scripting and only
simple reusable configuration. Deployment and distribution should
still be done with other tools. It can create simple Makefiles, A-A-P
files, and graph dependencies using DOT (graphviz) graphs.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/ccbuild

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.5.4-2
- Fix group tag.

* Thu May 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.5.4-1
- Updated to release 1.5.4.

* Wed Dec 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.5.2-1
- Initial package.
