# $Id$
# Authority: dag
# Upstream: <gaphor-list$lists,sf,net>

Summary: Graphical UML modeling environment
Name: gaphor
Version: 0.3.1
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://gaphor.sourceforge.net/

Source: http://dl.sf.net/gaphor/gaphor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnome-python2-diacanvas
Requires: gnome-python2-diacanvas

%description
Gaphor is a new project. The goal is to create an easy to use modeling
environment. This means that you are able to create nice UML diagrams
for documentation and to assist you with design decisions. Gaphor will
help you create your applications.

%prep
%setup

### FIXME: Created files needed by setup.py. (Please fix upstream)
touch data/gaphor-main-ui.xml \
	data/gaphor-diagram-ui.xml \
	data/gaphor-editor-ui.xml \
	data/gaphor.dtd

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install \
	--root="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS PKG-INFO README TODO doc/*.txt
%{_bindir}/*
%{_datadir}/gaphor/
%{_libdir}/python*/site-packages/gaphor/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1.2
- Rebuild for Fedora Core 5.

* Mon Apr 19 2004 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Updated to release 0.3.1.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Initial package. (using DAR)
