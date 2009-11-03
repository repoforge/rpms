# $Id$
# Authority: dag

%define real_name jEdit
%define real_version 42

Summary: Programmer's text editor written in Java
Name: jedit
Version: 4.2
Release: 2%{?dist}
License: GPL
Group: Applications/Editors
URL: http://www.jedit.org/

Source: http://dl.sf.net/jedit/jedit%{real_version}source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: ant
BuildRequires: docbook-style-xsl
BuildRequires: java >= 1.4.2
BuildRequires: libxslt

%description
jEdit is an Open Source, cross platform text editor written in Java. It
has an extensive feature set that includes syntax highlighting, auto indent,
folding, word wrap, abbreviation expansion, multiple clipboards, powerful
search and replace, and much more.

Futhermore, jEdit is extremely customizable, and extensible, using either
macros written in the BeanShell scripting language, or plugins written
in Java.

%prep
%setup -n %{real_name}

%{__cat} <<'EOF' >jedit.sh
#!/bin/sh

### Java heap size, in megabytes
JAVA_HEAP_SIZE="32"

### Java home directory
if [ "$JAVA_HOME" ]; then
    exec "$JAVA_HOME/bin/java" -mx${JAVA_HEAP_SIZE}m -jar %{_datadir}/jedit/jedit.jar $@
else
    echo "Warning: JAVA_HOME environment variable not set." >&2
    exec java -mx${JAVA_HEAP_SIZE}m -jar %{_datadir}/jedit/jedit.jar $@
fi
EOF

%build
ant
ant -f jars/LatestVersion/build.xml
ant -f jars/QuickNotepad/build.xml
ant -Ddocbook.xsl=/usr/share/sgml/docbook/xsl-stylesheets docs-html javadoc

### Create installer filelists
sh installer/mk_filelist.sh

%install
%{__rm} -rf %{buildroot}
java -classpath . installer.Install auto %{buildroot}%{_datadir}/jedit %{buildroot}%{_bindir}

%{__install} -Dp -m0755 jedit.sh %{buildroot}%{_bindir}/jedit
%{__install} -Dp -m0644 jedit.1 %{buildroot}%{_mandir}/man1/jedit.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.SRC.txt doc/*
%doc %{_mandir}/man1/jedit.1*
%{_bindir}/jedit
%{_datadir}/jedit/

%changelog
* Thu Apr 10 2008 Dag Wieers <dag@wieers.com> - 4.2-2
- Fix typo in wrapper script.

* Wed Apr 09 2008 Dag Wieers <dag@wieers.com> - 4.2-1
- Initial package. (using DAR)
