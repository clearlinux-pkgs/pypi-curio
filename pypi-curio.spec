#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-curio
Version  : 1.5
Release  : 15
URL      : https://files.pythonhosted.org/packages/bc/bc/2c438a1e8402a45b3f1a27abf45e3f280004c28d7bec6e2d1d8eb964a3cc/curio-1.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/bc/bc/2c438a1e8402a45b3f1a27abf45e3f280004c28d7bec6e2d1d8eb964a3cc/curio-1.5.tar.gz
Summary  : Curio
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-curio-license = %{version}-%{release}
Requires: pypi-curio-python = %{version}-%{release}
Requires: pypi-curio-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: curio
Provides: curio-python
Provides: curio-python3

%description
Curio is a coroutine-based library for concurrent systems programming.

%package license
Summary: license components for the pypi-curio package.
Group: Default

%description license
license components for the pypi-curio package.


%package python
Summary: python components for the pypi-curio package.
Group: Default
Requires: pypi-curio-python3 = %{version}-%{release}

%description python
python components for the pypi-curio package.


%package python3
Summary: python3 components for the pypi-curio package.
Group: Default
Requires: python3-core
Provides: pypi(curio)

%description python3
python3 components for the pypi-curio package.


%prep
%setup -q -n curio-1.5
cd %{_builddir}/curio-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641426323
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-curio
cp %{_builddir}/curio-1.5/LICENSE %{buildroot}/usr/share/package-licenses/pypi-curio/75e69fdeb32f462f776d12ac04dc06bc5ab9e68e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-curio/75e69fdeb32f462f776d12ac04dc06bc5ab9e68e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
